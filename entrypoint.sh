#/bin/bash

# In docker sometime the packages needs to updated
# pip install -r dependencies/requirements.txt

# Collect static files into static root
python src/manage.py collectstatic --noinput

# Start django development server
# python src/manage.py runserver

# Start the production server
gunicorn --chdir src core.wsgi:application --keep-alive 600 --pid pid/gunicorn.pid --user rx7 --group rx7 --access-logfile log/gunicorn/access.log --error-logfile log/gunicorn/error.log --reload --daemon
