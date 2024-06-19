from flask import Flask, render_template, request, flash, redirect, url_for
import eventlet
from eventlet import wsgi

from flask_socketio import SocketIO
from flask_socketio import emit


app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    wsgi.server(eventlet.listen(("192.168.X.X", 5000)), app)