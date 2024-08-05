#!/bin/bash

# Kemas kini dan pasang kebergantungan sistem
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver
pip install selenium requests-html

# Pasang kebergantungan Python
pip install -r requirements.txt
