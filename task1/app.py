import os
from flask import Flask
app = Flask(__name__)

city = (os.environ['CITY'])


@app.route('/')
def hello_world():
    return 'Hello, %s!' % city


if __name__ == '__main__':
    app.run()
