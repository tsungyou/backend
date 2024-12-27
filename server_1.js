const express = require("express");
const { Server: WebSocketServer } = require("ws");
const { Client } = require("pg");
const strategyRoute = require("./routes/priceRoute");
const config = require("./config/config");
const PORT = 3001;

const app = express();

const server = app.listen(PORT, () => {
    console.log(`Listening on ${PORT}`);
});

const wss = new WebSocketServer({ server });

const pgClient = new Client(config.db);

pgClient.connect()
    .then(() => {
        pgClient.query('LISTEN new_message_channel');
        console.log("Connected to PostgreSQL!");

        pgClient.on("notification", (msg) => {
            wss.clients.forEach((client) => {
                if (client.readyState === client.OPEN) {
                    client.send(`${msg.payload}`);
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

app.use(strategyRoute);

let counter = 1; 

function insertNewData() {
    // Create the message using the counter value
    const message = `${counter}`;
    const currentTime = new Date().toLocaleString("en-US", { timeZone: "Asia/Taipei" });

    pgClient.query(`INSERT INTO public.block_code3_deatil (code, da, cl) VALUES ($1, $2, $3)`, ["2330", currentTime, 111])
        .then(() => {
            console.log(`Inserted new data: ${message}`);
        })
        .catch(err => console.error("Error inserting data:", err));

    counter++;
}

setInterval(insertNewData, 10000);
