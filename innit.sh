python3 -m venv .venv

. .venv/bin/activate

pip install Flask

pip install Flask Flask-SQLAlchemy
pip install mysql-connector-python
pip freeze > requirements.txt


