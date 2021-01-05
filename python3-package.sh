#!/bin/bash

# 1. Create a lib folder by running this command:
LIB_DIR=python-package
mkdir -p $LIB_DIR

# 2. Install the library to LIB_DIR by running this command:
pip3 install psutil -t $LIB_DIR
pip3 install loguru -t $LIB_DIR
