#!/usr/bin/env bash

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

echo "======================================================"
echo "Running flake8"
echo "======================================================"
flake8

echo "======================================================"
echo "Running"
echo "======================================================"
python goreba_global/manage.py runserver

echo "======================================================="
echo "The server at http://127.0.0.1:8000/ is now accessible"
echo "======================================================="
