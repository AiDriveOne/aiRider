const express = require("express");
const http = require("http");
const socketIO = require("socket.io");

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

// Serve the frontend
app.use(express.static(__dirname + "/public"));

// Initialize the shared content
let sharedContent = "";

// Listen for WebSocket connections
io.on("connection", (socket) => {
  // Send the current content to the new client
  socket.emit("content-update", sharedContent);

  // Receive content updates from clients
  socket.on("content-update", (content) => {
    sharedContent = content;

    // Broadcast the updated content to all connected clients
    io.emit("content-update", sharedContent);
  });
});

// Start the server
const port = 3000;
server.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
