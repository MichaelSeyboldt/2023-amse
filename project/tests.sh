#!/bin/bash
cd ../data
if [ -f .venv/bin/activate ]; then
source .venv/bin/activate;
fi

make clean
ret=$?
if [ $ret -ne 0 ]; then
    echo "make clean failed"
    exit $ret
fi
make
ret=$?
if [ $ret -ne 0 ]; then
    echo "make failed"
    exit $ret
fi
python3 test.py
ret=$?
if [ $ret -ne 0 ]; then
    echo "tests failed"
    exit $ret
fi
if [ -f .venv/bin/activate ]; then
deactivate;
fi
