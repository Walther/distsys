# Distributed Temperature Service

## Description

- Temperature sensor network
- Each node has a fake temperature sensor and is located at a city
- Each node has a web service
  - Shows current temperature at the node
  - Shows the temperature of the other nodes, if available

## Usage with Docker

- Install [Docker](https://www.docker.com)
- Install `docker-compose`
- Run `docker-compose up` to start the service
- Run `docker-compose down` to delete the containers and clean up
- Run `docker-compose build` if you have made changes that need to be built into the image, e.g. changes to `requirements.txt` or Docker-related files

## Usage without Docker

- Install `python3`
- Install the requirements `pip3 install -r requirements.txt`

Run in two separate terminal windows:

- `CITY=helsinki PORT=5001 OTHER_HOSTS=localhost:5002 python3 app.py`
- `CITY=turku PORT=5002 OTHER_HOSTS=localhost:5001 python3 app.py`

This will get you two nodes running at `localhost:5001` and `localhost:5002` both polling each other for updates.

## TODO

- [x] Node has a `/` API endpoint that responds with an index page
- [x] Node has an `/api/currentTemp` that responds with a measurement object (e.g. `{"city": "Helsinki", celsius: 20.5, timestamp: "2019-11-08 16:36:08+02:00"}`)
- [x] Node has an `/api/selfWeatherHistory` that responds with a full history of its own temperature objects
- [x] Node periodically checks for the `/api/selfWeatherHistory` of the other nodes, and merges those into its knowledge of other nodes' history
- [x] Node has an `/api/othersWeatherHistory` that responds with a full history it has saved from other nodes
- [x] **IMPORTANT**: Deliverables, as defined by the exercise document!
- [ ] Optional: Pretty display of data? Temperature graphs?
- [ ] Optional: make the temperature adjust by small amounts, instead of jumping to random value
- [ ] Complicated, optional: Using `othersWeatherHistory` for the data fetches between nodes, so that node A can get information about node C by asking node B. This could require more complicated deduplication, could be significant performance hit, etc.
- [ ] Other ideas? Add to this list!
