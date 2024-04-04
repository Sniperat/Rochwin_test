FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nginx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py collectstatic --noinput

RUN until nc -z -v -w30 db 5432; do echo "Waiting for PostgreSQL server..."; sleep 5; done

# RUN python manage.py migrate
# RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'admin@example.com', 'Qwerty123$')" | python manage.py shell

EXPOSE 8000

CMD ["gunicorn", "--config", "gunicorn_config.py", "app.wsgi:application"]