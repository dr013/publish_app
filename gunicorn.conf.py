import multiprocessing

bind = "0.0.0.0:4000"

# bind = "unix:///srv/publish-app/publish-app.sock"
# worker numbers 2xCPUs + 1
workers = multiprocessing.cpu_count() * 2 + 1
user = "www-data"
group = "www-data"
errorlog = "/srv/publish-app/logs/error-gunicorn.log"
loglevel = "info"
proc_name = "publish-app"
accesslog = "/srv/publish-app/logs/access-gunicorn.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
