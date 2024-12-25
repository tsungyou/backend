const express = require("express");
const { Server: WebSocketServer } = require("ws");
const PORT = 3000;

const app = express();

// Start an HTTP server using Express
const server = app.listen(PORT, () => {
    console.log(`Listening on ${PORT}`);
});

// Attach WebSocketServer to the existing HTTP server
const wss = new WebSocketServer({ server });

wss.on("connection", (ws) => {
    console.log("Client connected");

    ws.on("message", (data) => {
        data = data.toString();
        console.log(data);

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
