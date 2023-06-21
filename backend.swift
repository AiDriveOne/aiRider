import Kitura
import Starscream

var sharedContent = ""

let router = Router()

router.all("/", middleware: StaticFileServer())

let server = WebSocketServer()

server.onConnect = { (socket) in
    socket.send(sharedContent)
}

server.onText = { (socket, text) in
    sharedContent = text
    socket.send(sharedContent)
}

server.onError = { (socket, error) in
    print("WebSocket encountered an error: \(error)")
}

server.onClose = { (socket, code, reason, clean) in
    print("WebSocket closed with code: \(code), reason: \(reason)")
}

server.onPing = { (socket) in
    socket.pong()
}

router.get("/websocket", handler: { (request, response, next) in
    server.handleUpgrade(request: request, response: response)
    next()
})

Kitura.addHTTPServer(onPort: 3000, with: router)
Kitura.run()
