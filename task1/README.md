# Distributed Temperature Service

## Description

- Temperature sensor network
- Each node has a fake temperature sensor and is located at a city
- Each node has a web service
  - Shows current temperature at the node
  - Shows the temperature of the other nodes, if available

## Installation

- Install [Docker](https://www.docker.com)
- Install `docker-compose`
- Run `docker-compose up` to start the service
- Run `docker-compose down` to delete the containers and clean up

## TODO

### Version 1
- [ ] Node has a `/` API endpoint that responds with an index page
- [ ] Node has an `/api/currentTemp` that responds with a measurement object (e.g. `{"node": "Helsinki", kelvins: 273.15, timestamp: "2019-11-08 16:36:08+02:00"}`)
- [ ] Index page lists current temperature of all known nodes

## Version 2
- [ ] Node has an `/api/tempHistory` that responds with a full history of its own temperature objects
- [ ] Node periodically checks for the history of other nodes, and intelligently merges that into its knowledge of other nodes' history
- [ ] Node has an `/api/distributedHistory` (TODO: better name?) that responds with a full history it has saved from other nodes. This makes it possible for node A to get information of node C by asking node B, etc
- [ ] more?

etc
