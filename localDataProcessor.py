#!/usr/bin/env python
# coding: utf-8
import csv
import hashlib
from datetime import datetime

import pandas as pd
from faker import Faker


def hash_sha256(val):
    """
    Function to hash the value using sha256 algorithm
    """

    return hashlib.sha3_256(val.encode()).hexdigest()


def annonymise_data(input_filepath="./data.csv", output_filepath="./output.csv", 
                   index=False, columns_to_annonymise=[], annonymised_func=hash_sha256):
    """
    Function to annonymise the data based on the annonymised function passed,
    and column names specified and writes out a csv file to the given location
    """
    
    data = pd.read_csv(input_filepath)
    for col in columns_to_annonymise:
        data[col] = [annonymised_func(val) for val in data[col]]
    data.to_csv(output_filepath, index=index)

if __name__ == "__main__":
    fake = Faker(['it_IT', 'en_US', 'ja_JP'])
    num_records = 1000000 #creating 1 million records
    first_name_column = "first_name"
    last_name_column = "last_name"
    address_column = "address"
    date_of_birth_column = "date_of_birth"
    data_file_path = "./customerdata.csv"
    processed_file_path="./annonymised.csv"
    columns_to_annonymise = [first_name_column, last_name_column, address_column]   

    with open (file=data_file_path,mode="w", encoding="utf-8") as file:
        field_names = [first_name_column, last_name_column, address_column, date_of_birth_column]
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        for _ in range(0, num_records):
            writer.writerow({
                first_name_column: fake.first_name(),
                last_name_column: fake.last_name(),
                address_column: fake.address(),
                date_of_birth_column: datetime.strftime(fake.date_of_birth(), "%d-%m-%Y")
            })

    annonymise_data(input_filepath=data_file_path,
                output_filepath=processed_file_path,
                columns_to_annonymise=columns_to_annonymise)

