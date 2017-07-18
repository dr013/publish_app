#!/usr/bin/sh
cd /srv/publish-app/
/usr/bin/nohup /srv/publish-app/venv/bin/gunicorn main:app -c gunicorn.conf.py 
