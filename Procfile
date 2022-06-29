web: gunicorn bam_api.wsgi
release: python3.8 manage.py makemigrations --noinput
release: python3.8 manage.py collectstatic --noinput
release: python3.8 manage.py migrate --noinput