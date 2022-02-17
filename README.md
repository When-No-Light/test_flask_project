# Project Title

Simple Flask Rest API

## Description

The application allows you to get a list of available moves for chess pieces using //http requests.

## Getting Started

### Dependencies

* Python 3.9
* Docker

### Installing

* open project folder and create new env with command `virtualenv env`
* activate env `env\Scripts\activate`
* install dependencies `pip install -r requirements.txt`

### Executing program

* run app with command `flask run`
* to run test `pytest app/test.py`

### Runing program in docker

* open project folder and run command `docker build -t flask-rest-api .`
* run app `docker run -d -p 5000:5000 flask-rest-api`

