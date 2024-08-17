#! /usr/bin/env bash

set -e

sudo apt update -y
sudo apt install -y pkg-config libhdf5-dev 
pip3 install -r requirements.txt