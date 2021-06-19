#!/bin/bash
clusterId=($(jq -r '.ClusterId' cluster.json))
echo "terminating the cluster ${clusterId}"
aws emr terminate-clusters --cluster-ids $clusterId

#remove the cluster json file
rm cluster.json

#remove the local data and data in s3
rm -r ./annonymised.csv 
aws s3 rm s3://nakuldefaultest/annonymised --recursive
aws s3 rm s3://nakuldefaultest/customerdata.csv
