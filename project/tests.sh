#!/bin/bash
cd ../data
source .venv/bin/activate
make
python3 test.py
deactivate 
