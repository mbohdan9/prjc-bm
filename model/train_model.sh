#!/bin/bash

# Create a Python virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the dependencies from requirements.txt
pip install -r requirements.txt

# Run the Python script
python train.py

# Deactivate the virtual environment
deactivate
