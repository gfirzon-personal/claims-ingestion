import csv
import json

class BatchCsvParsingService:
    def __init__(self):
        pass

    def get_headers(self, file_path):
        # Open and read the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Skip the header row
        
            #return [dict(zip(headers, row)) for row in csv_reader]        
            return headers
        
    def get_data(self, file_path):
        # List to store each record as a dictionary
        data_list = []

        # Open and read the CSV file
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)  # Skip the header row
        
            for row in csv_reader:
                # Combine headers with row data into a dictionary
                record = dict(zip(headers, row))
                data_list.append(record)  

        return data_list

    # def parse(self) -> List[Dict[str, str]]:
    #     with open(self.csv_file_path, newline='') as csvfile:
    #         csvreader = csv.DictReader(csvfile)
    #         return list(csvreader)