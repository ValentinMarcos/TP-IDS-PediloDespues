#!/bin/bash

python3 -m venv .venv

. .venv/bin/activate

pip install Flask
pip install requests
pip install user-agents
pip install geopy


pip freeze > requirements.txt


