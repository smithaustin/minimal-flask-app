# minimal-flask-app
This repo provides a minimal flask app with SQLalchemy setup with migrations and models.

## Installation and Requirments

Requires minimum Python 3.7. It is recommended to use virtualenv

To install requirements:

    pip install -r requirements.txt

## Migration

If starting from scratch, assure the database exists and run 
    
    python app.py db init

To generate a new migration after changing models,

    python app.py db migrate -m "migration description"

To upgrade the db to the newest migration,

    python app.py db upgrade

If the migration doesn't capture some of your changes (apparently alimibic can't detect table name changes for example), create a blank revision with:

    python app.py db revision -m "migration description"

## Running app in dev

    python app.py dev
