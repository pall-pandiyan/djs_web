#/bin/bash

gunicorn --chdir ./src core.wsgi:application --keep-alive 600 --pid ../pid/gunicorn.pid --user rx7 --group rx7 --access-logfile ../log/gunicorn/access.log --error-logfile ../log/gunicorn/error.log --reload --daemon
