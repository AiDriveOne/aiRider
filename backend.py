# Save this code in backend.py
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

shared_content = ""

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('content-update')
def handle_content_update(content):
    global shared_content
    shared_content = content
    emit('content-update', shared_content, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
