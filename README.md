Requirements
============

You need a python3 development environment and a redis-server

Install
=======

It's better to be on a virtual environment.

Install dependencies : `pip install -r requirements.txt`

Run server
==========

`gunicorn aligments_backend.main:app`

Example
=======

Add a notion
------------

`curl -H "Content-Type: application/json" -H "Accept: application/json" -X POST -d '["", ]' http://163.172.140.176/notions/`

Query a notion
---------------

`curl -H "Accept: application/json" -X GET http://localhost:8000/notions/uri=http://1`
