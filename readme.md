# Object Report

A Django Restful API for reporting of class object creation, update, or deletion. Along with the API container, there is also a mongodb container and a mongo-express container.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
For API:
  Docker
  Docker-Compose
For Test Script:
  pip3 install request
```

### Installing

A step by step series of examples that tell you how to get a development env running

```
#From Root Directory EvidenceCare
docker-compose build
docker-compose up
```
This should spawn three containers:
1. Mongodb: exposed only through the docker network and creates a DB named 'objectreport'
2. Mongo-Express: exposed on http://0.0.0.0:8081/ (view objectreport at http://0.0.0.0:8081/db/objectreport)
3. Object Report API: exposed through http://0.0.0.0:8000/report/

## Running the tests

To run a test script:

```
#From Root Directory EvidenceCare
python3 test.py
```

## Notes

Thanks for taking the time to evaluate my code! I choose Django and Mongo based off my knowledge of EvidenceCare's techstack.
Hopefully everything was able to spin up correctly and pretty easy if docker and docker-compose are installed. I took a few
liberties when deciding how to set this up:

  1. Mongo - Give the volatility of objects within Python, I think reddis maybe a better choice as a database given how fast
             it is compared to mongo. This could even be setup to purge old entries after a certain time or volume that would
             be beneficial.

  2. Threading - I used gunicorn to spawn up a few workers as a proof of concept. This could become an issue with race cases
                 in the database and cause issues with updating or creating. This possibly could be fixed with some logic
                 based the timestamp in the give entry.

  3. Class Save/Delete - This was an issue that needs to be looked at later on. In my mind, these functions should be as
                         light weight as possible. I tried to send the python object as a binary field within the json
                         request but I was getting a type error and couldn't send the binary data like I had planned.

  4. Use case - When deciding how to design the API, I choose to just make a base restful API to handle all the marshaling
                of data. This works but I honestly feel like spinning this up as its own service might be too much for such a
                lightweight application. I would envision this as more of a sidecar to be deployed along side a docker
                container in a pod to handle the request. This could also just be a lambda function. A caveat with lambda would
                be race cases but that can be taken care of as stand above.

  5. Unique Identifier - This honestly was one of the trickiest parts of the assessment. Give how I set it up, I tried to make
                         it as simple as possible by using the PID of the applcation and the object id. This could cause some
                         issues with the object id being reusable in python as well as the PID being reused. This would need
                         to be looked at for a more elegant solution. One fix could be use the docker container ID but I'm un
                         sure of a better way to uniquely identify an object within Python other than keeping track of
                         enumerated id.


## Built With

* [Django] - The web framework used
* [Django Restful Framework] - The restful framework
* [Mongo] - Database

## Authors

* **Ian Ezell**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
