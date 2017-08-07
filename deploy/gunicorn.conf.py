import multiprocessing

# bind = "unix:///srv/publish-app/publish-app.sock"
bind = "unix:///srv/publish-app/publish-app.sock"
# bind = "0.0.0.0:4000"

# worker numbers 2xCPUs + 1
workers = multiprocessing.cpu_count() * 2 + 1

user = "www-data"
group = "www-data"

timeout = 120
# reload = True

accesslog = "/srv/publish-app/logs/access-gunicorn.log"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
errorlog = "/srv/publish-app/logs/error-gunicorn.log"
loglevel = "info"

proc_name = "publish-app"
