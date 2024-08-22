#!/bin/bash

python3 -m venv shinCity

# Ensure the virtual environment is activated only once
source shinCity/bin/activate

# Install necessary packages
pip3 install pygame pillow

# Virtual environment should remain activated here
echo "Virtual environment activated with necessary packages installed."
