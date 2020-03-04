# Trambo-Docker-Compose
Marzo 4, 2020. Ejercicio de docker compose

## Introduction
To solve this problem, i use the following technologies:
- Flask: is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

- Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache.

- Redis is an in-memory data structure project implementing a distributed, in-memory key-value database with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indexes.


Nginx where used in this solution as a :
- web server: Serve all static files.
- reverse proxy: Redirect traffic to specific webserver (could be nginx used to serve static content or python flask app)


## Folder Hierarchy

```
Docker-Compose
│   README.md
│   docker-compose.yml    
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