from flask import Flask
app = Flask(__name__)

# establish a route / define the starting point
@app.route('/')

def hello_world():
    return 'Hello World'