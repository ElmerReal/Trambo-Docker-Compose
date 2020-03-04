# Trambo-Docker-Compose
Marzo 4, 2020. Ejercicio de docker compose

## Introduction
To do this exercise, i used the following technologies/tools:
- Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

- Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.

- Redis is an in-memory data structure project implementing a distributed, in-memory key-value database with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indexes.

- Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

- Docker Compose  is a tool for defining and running multi-container Docker applications.

A brief explanation of what the exercise consist is:

- There have to be a redis container, which will store data sended by the flask container.
- There have to be a nginx container, which will serve static files to the user.
- There have to be another nginx container, which will work as a proxy in order to redirect the trafic to the flask container or the nginx static files container dependin on a specific prefix. 


## Folder Hierarchy

```
./
│   README.md
│   [docker-compose.yml](/docker-compose.yml)
│
└───flaskserver
│   |   app.py
│   |   Dockerfile
|   |   requirements.txt
|   
└───nginx_proxy
│   │   Dockerfile
│   │
│   └───proxyfiles
│       │   reverse-proxy.conf
│   
└───nginx_static
    │   Dockerfile
    |
    └───page
        │   index.html 
```

### [docker-compose.yml](/docker-compose.yml)