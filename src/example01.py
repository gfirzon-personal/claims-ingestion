import csv
import numpy as np
#print("Hello World")
#print(f"The sum of 2 and 4 is {2 + 4}")

file_name = "generated_batch_sample.csv"
file_path = f"./data/{file_name}"
 
# Reading a CSV file
# with open(file_path, mode='r') as file:
#     csv_reader = csv.reader(file)
#     for row in csv_reader:
#         print(row)

with open(file_path, mode='r') as file:
    headers = file.readline().strip().split(',')  # Read the first line and split
    print("Column Headers:", headers)
