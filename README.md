# Annonymise data processing

The purpose of this project to demonstrate ability to annonymise data locally and on a distributed system

## Motivation

The motivation behind this project is to show others how easy it is to do a POC on local machine using python, and when need is there to process big data, how can utilise a spark framework

## Built With

The section covers tools used to enable the project.

1. Python to create csv and annonymise data locally
2. Amazon EMR to process big data and output to s3
3. PySpark to process and carry out processing
4. Bash to create the infrastructure, move data to s3 and delete the infrastructure, and local and s3 files

## Project Files and Folders

1. localDataProcessor.py - Contains all the logic to create the local csv and annonymise data locally.
2. sparkDataProcessor.py - Contains all the logic to read file from distributed file system S3, and process it using spark framework
3. sparkSubmit.sh - Shell file that will get executed on the emr cluster and will call the spark submit on the cluster and will run the sparkDataProcessor.py
4. runSparkEmrCluster.sh - Contains the pipeline to automate infrastructure requirements which will create the emr cluster, load the sparkDataProcessor.py file on the cluster and load data from s3 into user specific s3 bucket
5. destroyResources.sh - Contains the pipeline to destroy the infratsructure associated with the project, and remove all the files created locally and on s3.
6. datamover.sh - Install python dependencies, runs the local data processor and pushes the local data to s3 bucket.
7. requirements.txt - Python library dependencies file, to make sure have all packages to run locally

## Running the pipeline

1. Create the editor role in aws iam
2. Configure the aws cli with the editor role access key and secret.
3. Run datamover.sh to push local data to S3. This will run the local data
   ```bash
   bash datamover.sh
   ```
4. Create the ssh key pair for ec2 instance using aws cli, give it a name such as my-key-pair. Make sure key is stored in root directory and is in the same region in which emr cluster/ec2 instances will be created.
   ```bash 
   aws ec2 create-key-pair --key-name my-key-pair --query "KeyMaterial" --output text > my-key-pair.pem
   ```
5. If you're connecting to your instance from a Linux computer, it is recommended that you use the following command to set the permissions of your private key file so that only you can read it.
   
   ```bash
   chmod 400 MyKeyPair.pem
   ```

6. Open terminal
7. Run runSparkEmrCluster.sh script to create the emr cluster and execute the spark job on the cluster
   .Pass the cluster name as first choice of argument and name of the key associated with ec2 instance

    ```bash 
    bash runSparkEmrCluster.sh <cluster_name> <keyName>
    ```


## Destroying the infrastructure to avoid costs

1. Run the destroyResources.sh that will terminate the cluster
   
    ```
    bash destroyResources.sh
    ```
 
# Contact for questions or support

Nakul Bajaj
bajaj.nakul@gmail.com
