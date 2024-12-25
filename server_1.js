const express = require("express");
const { Server: WebSocketServer } = require("ws");
const { Client } = require("pg");
const PORT = 3001;

const app = express();

const server = app.listen(PORT, () => {
    console.log(`Listening on ${PORT}`);
});

const wss = new WebSocketServer({ server });

const pgClient = new Client({
    user: 'mini',
    host: 'localhost',
    database: 'tw',
    password: 'buddyrich134',
    port: 5432,
});

pgClient.connect()
    .then(() => {
        pgClient.query('LISTEN new_message_channel');
        console.log("Connected to PostgreSQL!");

        pgClient.on("notification", (msg) => {
            console.log("Received notification: ", msg.payload);
            wss.clients.forEach((client) => {
                if (client.readyState === client.OPEN) {
                    client.send(`New message in the database: ${msg.payload}`);
                }
            });
        });
    })
    .catch(err => console.error("Failed to connect to PostgreSQL:", err));

// WebSocket connection
wss.on("connection", (ws) => {
    console.log("Client connected");

    ws.on("message", (data) => {
        data = data.toString();
        console.log("Received message:", data);

        // Echo the message back to the sender
        ws.send(data);

        // Broadcast the message to all clients
        wss.clients.forEach((client) => {
            if (client !== ws && client.readyState === ws.OPEN) {
                client.send(data);
            }
        });
    });

    ws.on("close", () => {
        console.log("Connection closed");
    });
});
let counter = 1;  // Initialize the counter to 1

// Function to insert new data (for testing)
function insertNewData() {
    // Create the message using the counter value
    const message = `Message ${counter}`;
    
    // Insert the message into the database
    pgClient.query(`INSERT INTO messages (content) VALUES ($1)`, [message])
        .then(() => {
            console.log(`Inserted new data: ${message}`);
        })
        .catch(err => console.error("Error inserting data:", err));

    // Increment the counter for the next message
    counter++;
}

// For demonstration purposes, let's insert new data every 5 seconds
setInterval(insertNewData, 5000);
