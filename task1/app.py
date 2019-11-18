from threading import Timer
import os
import random
import time
import datetime
import requests
import uuid
from flask import Flask, render_template, jsonify

# Globals
app = Flask(__name__)
city = (os.environ['CITY'])
port = int((os.environ['PORT']))
other_hosts = (os.environ['OTHER_HOSTS']).split(",")
temp = None
timestamp = None
self_weather_history = []
others_weather_history = []
his_length = 10
# Set retry options to maximum of 1
requests_session = requests.Session()
requests_adapter = requests.adapters.HTTPAdapter(max_retries=1)
requests_session.mount('http://', requests_adapter)


# Repeating threaded timer borrowed https://stackoverflow.com/a/48741004/3709997
class RepeatTimer(Timer):
    def run(self):
        while not self.finished.wait(self.interval):
            self.function(*self.args, **self.kwargs)


# Generates a new temperature
def new_temperature():
    return random.normalvariate(15, 5)


# Generates a new ISO8601 timestamp with local timezone information
def new_timestamp():
    return datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()


# Generates a new "temperature recording"
# Updates the global variables temp and timestamp
# Saves the recording to global variable self_weather_history
def create_temp_update():
    global temp, timestamp, self_weather_history, his_length
    temp = new_temperature()
    timestamp = new_timestamp()
    measurement = {
        'uuid': uuid.uuid4(),
        'celsius': temp,
        'city': city,
        'timestamp': timestamp
    }
    self_weather_history.append(measurement)
    


# Tries to fetch the weather history from other nodes
# The data request is allowed to fail
def fetch_history_from_other_nodes():
    # NOTE: always fetches all of the history for all nodes
    # Could be optimized by adding logic to only fetch data newer than our
    # newest data point from the node
    global others_weather_history, his_length
    for host in other_hosts:
        try:
            r = requests.get("http://" + host + "/api/selfWeatherHistory")
            data = r.json()
            combined = others_weather_history + data
            # This deduplicates the history using the uuid as the key
            # https://stackoverflow.com/a/11092590/3709997
            others_weather_history = list(
                {v['uuid']: v for v in combined}.values())
        except Exception as e:
            print("Could not load data from {} - {}".format(port, e))


@app.route('/api/currentTemp')
def get_current_temp():
    return jsonify(self_weather_history[-1])


@app.route('/api/selfWeatherHistory')
def get_self_weather_history():
    if len(self_weather_history) > his_length:
        show_self_weather_history = self_weather_history[-his_length:]
    else:
        show_self_weather_history = self_weather_history
    return jsonify(show_self_weather_history)


@app.route('/api/othersWeatherHistory')
def get_others_weather_history():
    if len(others_weather_history) > his_length:
        show_others_weather_history = others_weather_history[-his_length:]
    else:
        show_others_weather_history = others_weather_history
    return jsonify(list(show_others_weather_history))


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # Run once at startup to set initial temperature, timestamp, and history
    create_temp_update()

    # This timer calls create_temp_update every 5 seconds
    measurement_timer = RepeatTimer(5, create_temp_update)
    measurement_timer.start()

    # Create another timer that calls fetch_history_from_other_nodes every 10 seconds
    fetch_others_timer = RepeatTimer(10, fetch_history_from_other_nodes)
    fetch_others_timer.start()

    # Serve the web application
    app.run(host="0.0.0.0", port=port)
