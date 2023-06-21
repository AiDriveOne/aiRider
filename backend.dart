// Save this code in backend.dart
import 'package:shelf/shelf.dart' as shelf;
import 'package:shelf/shelf_io.dart' as io;
import 'package:shelf_web_socket/shelf_web_socket.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

import 'dart:io';

var sharedContent = '';

void main() async {
  var handler = webSocketHandler((WebSocketChannel webSocket) {
    webSocket.stream.listen((message) {
      sharedContent = message;
      webSocket.sink.add(sharedContent);
    });
  });

  var cascade = shelf.Cascade()
      .add(handler.handler)
      .add(shelf.createStaticHandler('web'));

  var server = await io.serve(cascade.handler, 'localhost', 3000);
  print('Server running on ${server.address.host}:${server.port}');
}
