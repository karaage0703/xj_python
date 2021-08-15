#!/bin/bash

echo -e "Clean up"
rm -rf dist/
rm -rf xj_python.egg-info/
python3 setup.py sdist