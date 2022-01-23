from flask import Flask, render_template
from flask_socketio import SocketIO,emit,send
from json import dump
from flask_bootstrap import Bootstrap5
from flask_pymongo import PyMongo



from insta_api import data_ca

ca = data_ca()

app = Flask(__name__)

app = Flask(__name__)
app.config["MONGO_URI"] = " mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb"
mongo = PyMongo(app)
bootstrap = Bootstrap5(app)

app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode=None)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insta_posts')
def test():
    return render_template('insta_posts.html',ca=ca)


###############socket###########
users = {}

@socketio.on('connected')
def connect(data):
    print(data)



@socketio.on('disconnect')
def disconnected(data_):
    print(data_)
    socketio.on('disconnect',data_)

if __name__ == '__main__':
    socketio.run(app)