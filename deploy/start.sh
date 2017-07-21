#!/bin/bash

cd /srv/publish-app/
/srv/publish-app/venv/bin/gunicorn main:app -c gunicorn.conf.py
