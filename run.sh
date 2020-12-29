#!/bin/bash
set -e
export FLASK_APP=zootube.py
flask run --host=0.0.0.0
