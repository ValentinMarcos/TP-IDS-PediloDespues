#!/bin/bash

python3 -m venv .venv

. .venv/bin/activate

pip3 install Flask
pip3 install requests

pip3 freeze > requirements.txt


