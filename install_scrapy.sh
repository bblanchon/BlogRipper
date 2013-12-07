#!/bin/bash
# tested on Ubuntu 13.10 "saucy" 

set -eu

sudo apt-get update

# PIP
sudo apt-get install python-setuptools python-dev libxml2-dev libxslt-dev libz-dev
sudo easy_install pip

# Scrapy
sudo pip install scrapy 