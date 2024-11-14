#!/bin/bash

python3 -m venv .venv

. .venv/bin/activate

pip install Flask
pip install requests

# Base de datos
pip install flask_sqlalchemy
pip install mysql-connector-python


pip freeze > requirements.txt