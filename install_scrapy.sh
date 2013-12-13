#!/bin/bash
# tested on Ubuntu 13.10 "saucy" 

set -eu

sudo apt-get update

# Install python developement libs
sudo apt-get install python-setuptools python-dev libxml2-dev libxslt-dev libz-dev

# Install Scrapy
sudo easy_install scrapy 