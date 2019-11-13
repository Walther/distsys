import os
import random
from flask import Flask
app = Flask(__name__)

city = (os.environ['CITY'])
temp = random.normalvariate(15, 5)

@app.route('/')
def hello_world():
    return 'Hello, %s! The temperature is currently %.1f degrees celcius.' % (city, temp)


if __name__ == '__main__':
    app.run()
