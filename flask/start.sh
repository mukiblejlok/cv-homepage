#! /usr/bin/env sh
set -e

# run upgrades and pre-fill db
flask deploy

# Start Gunicorn
exec gunicorn -k egg:meinheld#gunicorn_worker -c gunicorn_conf.py main:app
