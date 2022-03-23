# TFL Scheduler

This API can be used to schedule tasks that run against the TFL API and gather data. It's based on FastAPI and ABScheduler using Python.
It implements two endpoints from TFL `/Line/{ids}` and `Line/{ids}/Disruption`

The following are available through the API:

* Create a scheduled task to get data for 1 or multiple lines. If `schedule_time` exists the task will run when configured, otherwise it will run now.
* Update a scheduled task and edit `title`, `description`, `lines`, and `schedule_time`.
* Delete a scheduled task, which will also remove the scheduled job.
* Get one or more tasks
* Get results of one task

## How to start the server

### Local

The app uses a PostgreSQL running on localhost and on the default port `5432`. All the required information should be added to the `.env` file. Migrations should be run before starting the server with:

```console
alembic upgrade head
```

Locally the server can run with:

```console
uvicorn app.main:app --reload --host 0.0.0.0 --port 5555
```

### Using `docker-compose`

The project can also be spawned using `docker-compose` which will spawn a PostgreSQL, the app and will create a persistent volume. Only for the first time please set in .env `RUN_MIGRATIONS=1` for migrations to run and then change it to `RUN_MIGRATIONS=0` or delete it.

Executing the following command the app will be available after a couple of seconds in <http://localhost:5555>.

```console
docker-compose up -d
```

### Tests

Unfortunately I wasn't able to create a process for testing using a mock/dummy database. If you run tests, please keep in mind that the "production" database will be filled. Tests can be run by executing either

```console
pytest --cov=app --cov-report=html --cov-report=term-missing app/tests
```

or the test.sh inside the scripts folder.
