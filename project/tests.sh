#!/bin/bash
cd ../data
source .venv/bin/activate
make clean
make
python3 test.py
deactivate 
