#!/usr/bin/env bash

curl https://bootstrap.pypa.io/get-pip.py | python
pip install -r $1requirements/requirements.txt
