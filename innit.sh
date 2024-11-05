#!/bin/bash

project_folder_name=$1

if python3 --version ; then
    echo "Python installed"
else
    echo "Python will be installed"
    sudo apt install python3
fi

if pip3 --version ; then
   echo "Pip installed"
else
   echo "Pip will be installed"
   sudo apt install python3-pip
fi

sudo apt install python3.10-venv

mkdir $project_folder_name
cd $project_folder_name

python3 -m venv .venv

. .venv/bin/activate

pip3 install Flask
pip3 install requests

pip3 freeze > requirements.txt


