import os
import random, time, threading
from datetime import datetime
from flask import Flask, render_template, jsonify
app = Flask(__name__)

city = (os.environ['CITY'])
temp = random.normalvariate(15, 5)

def temp_update(first_time = False):
    app.config['updated'] = not first_time
    delay = 10
    threading.Timer(delay, temp_update).start()

@app.route('/currenttemp')
def data():
    nowstr = time.strftime("%a, %d %b %Y %H:%M:%S +0000")
    temp = random.normalvariate(15, 5)
    
    return jsonify({'contents': temp})

@app.route('/')
def hello_world():
    #current_time = str(datetime.utcnow())[:-7]
    #return 'Hello, %s! The temperature is currently %.1f degrees celcius. The time is %s.' % (city, temp, current_time)
    return render_template("index.html")

@app.route("/updated")
def updated():
    while not app.config['updated']:
        time.sleep(0.5)
    app.config['updated'] = False
    return "changed!"

if __name__ == '__main__':
    temp_update(first_time = True)

    app.run()
