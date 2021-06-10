release: python manage.py migrate
web: gunicorn adafruitapi.wsgi:application --log-file - --log-level debug

