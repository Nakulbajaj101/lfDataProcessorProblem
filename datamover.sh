#!/bin/bash 

pip install -r requirements.txt
python localDataProcessor.py

#push data to aws
aws s3 mv ./customerdata.csv s3://nakuldefaultest/
