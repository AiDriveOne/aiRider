import asyncio
import websockets

# Initialize the shared content
shared_content = ""

# WebSocket server handler
async def handle_websocket(websocket, path):
    global shared_content

    # Send the current content to the new client
    await websocket.send(shared_content)

    try:
        async for message in websocket:
            shared_content = message

            # Broadcast the updated content to all connected clients
            await asyncio.wait([ws.send(shared_content) for ws in websockets])

    except websockets.exceptions.ConnectionClosed:
        pass

# Start the WebSocket server
start_server = websockets.serve(handle_websocket, "localhost", 3000)

# Run the event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
