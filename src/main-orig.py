import csv
import json

file_name = "generated_batch_sample.csv"
output_file_name = "output.json"
file_path = f"./data/{file_name}"
output_file_path = f"./data/{output_file_name}"

# List to store each record as a dictionary

data_list = []

def file_writer(): 
    # Write to a JSON file
    with open(output_file_path, mode='w') as file:
        json.dump(data_list, file, indent=4)
    
    print("Data written to output.json")

def function2():
    # Open and read the CSV file
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Skip the header row
    
        for row in csv_reader:
            # Combine headers with row data into a dictionary
            record = dict(zip(headers, row))
            data_list.append(record)  

def function1():
     # Open and read the CSV file
    with open(file_path, mode='r') as file:
        # Use DictReader to read the CSV file as dictionaries
        csv_reader = csv.DictReader(file)
    
        for row in csv_reader:
        # Convert OrderedDict to a regular dictionary (optional)
            record = dict(row)
            data_list.append(record)
    
function2() 
  
# Print the list of dictionaries
#print(data_list)

file_writer()
