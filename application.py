from flask import Flask
application = Flask(__name__)

@application.route('/hello/')
def hello():
    return 'Bonjour tout le monde!'
