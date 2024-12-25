const WebSocket = require('ws');

const ws = new WebSocket('ws://localhost:3000'); // Connect to your WebSocket server

ws.on('open', () => {
    console.log('Connected to server');
    ws.send('Hello, Server!');
});

ws.on('message', (message) => {
    console.log(`Received: ${message}`);
});

ws.on('close', () => {
    console.log('Connection closed');
});
