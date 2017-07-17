#!/usr/bin/env python
# coding=utf-8
#  Created by 'Evgeny Krukov<krukov@bpcbt.com>' at 07.11.13 19:53<br />

import datetime
from fabric.api import env, run, cd, sudo, require, prefix
from fabric.colors import green, red
from fabric.contrib import django
from contextlib import contextmanager as _contextmanager

now = datetime.datetime.now()
django.project('rndgui')
django.settings_module('rndgui.settings')


def production():
    # здесь данные об удаленном сервере с сайтом
    env.environment = "production"
    env.hosts = ["sv2.bpc.in:22"]
    env.user = 'www-data'
    env.path = '/srv/publish-app'
    env.activate = 'source /srv/publish-app/venv/bin/activate'


@_contextmanager
def virtualenv():
    with cd(env.path):
        with prefix(env.activate):
            yield


def deploy():
    """
    In the current version fabfile no initial database creation and configure the virtual server host.
    """
    print(red("Beginning Deploy:"))
    update_from_git()
    install_requirements()
    stop_webserver()
    start_webserver()
    # touch_reload()
    status_webserver()


def install_requirements():
    print(green(" * install the necessary applications..."))
    if 'develop' in env.environment:
        req = 'dev.txt'
    else:
        req = 'prod.txt'
    with virtualenv():
        requirements_file = 'requirements/{req}'.format(req=req)

        args = ['install',
                '-r', requirements_file, '--upgrade'
                ]
        run('pip %s' % ' '.join(args))


def update_from_git():
    print(green('* update from git'))
    with cd(env.path):
        print(green('run checkout master'))
        run('git checkout -- .')
        run('git clean -fd')

        if 'develop' in env.environment:
            run('git checkout develop')
        else:
            run('git checkout master')

        run('git fetch --prune origin')
        run('git pull')


def touch_reload():
    print(green('touch reload uwsgi'))
    with cd(env.path):
        run("git show > uwsgi")


def stop_webserver():
    print(green('Stop Supervisord'))
    sudo("service supervisord stop")


def start_webserver():
    print(green('Stop Supervisord'))
    sudo("service supervisord start")
    sudo("service nginx restart")


def status_webserver():
    require('environment', provided_by=[production1, production2, dev])
    print(green('Status Supervisord'))
    sudo("service supervisord status")


def set_dev_config():
    print (green('Copy settings/dev'))
    with cd(env.path):
        run('cp rndgui/settings/demo.py rndgui/settings/dev.py')


def run_dev_server():
    print (green('Run dev server'))
    with virtualenv():
        run(
            '[ `pgrep -f "/srv/rndgui"` ] && echo "already worked" || nohup /srv/rndgui/venv/bin/python manage.py runserver sv2.bpc.in:8000 &')
