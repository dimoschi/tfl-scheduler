FROM python:3.10.2-slim

EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Upgrade pip
RUN python -m pip install --no-cache-dir --upgrade pip

# Install pip requirements
COPY ./requirements.txt /tmp/requirements.txt
RUN python -m pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./app /app
# COPY ./alembic /app/alembic
COPY ./alembic /alembic
COPY .env .env
# COPY alembic.ini /app/alembic.ini
# COPY alembic.ini /app/app/alembic.ini
COPY alembic.ini alembic.ini

COPY ./wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

ENV PYTHONPATH=/app

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]