#!/bin/bash

# Kemas kini dan pasang kebergantungan sistem
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver

# Pasang kebergantungan Python
pip install -r requirements.txt
