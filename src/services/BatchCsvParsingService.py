import csv
import json
import io

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
        
    def get_data_from_content(self, file_content):
        """
        Parse the CSV content and return a list of dictionaries
        where each dictionary represents a line in the CSV file.
        """

        # List to store each record as a dictionary
        data_list = []

        # Convert the string content to a file-like object
        file_like_object = io.StringIO(file_content)

        # Read the CSV content
        csv_reader = csv.reader(file_like_object)
        headers = next(csv_reader)  # Skip the header row

        for row in csv_reader:
            # Combine headers with row data into a dictionary
            record = dict(zip(headers, row))
            data_list.append(record)

        return data_list     

    def read_all_lines(self, file_content):
        """
        reads all lines of the file_content into a string array and returns it
        """

        # Convert the string content to a file-like object
        file_like_object = io.StringIO(file_content)

        # Read the CSV content
        csv_reader = csv.reader(file_like_object)
        headers = next(csv_reader)  # Skip the header row

        data_list = []
        lines = []
        result_list = []
        #lines.append(','.join(headers))  # Convert headers to a single line of text
        header_line = (','.join(headers))  # Convert headers to a single line of text
        #print("header_line", header_line)

        for row in csv_reader:
            # Convert row to a single line of text
            output = io.StringIO()
            csv_writer = csv.writer(output)
            csv_writer.writerow(row)
            #line = output.getvalue().strip()  # Get the CSV formatted line and strip any extra newline
            line = output.getvalue()  # Get the CSV formatted line and strip any extra newline
            #lines.append(line)

            # Combine headers with row data into a dictionary
            record = dict(zip(headers, row))
            #data_list.append(record)            
            result_list.append({
                "record": record,
                "line": line
            })
            #print("line:", line)
            #print("record:", record)

        print("creating result")

        result = {
            "result_list": result_list,
            "header_line": header_line
        }

        print("created result")
        return result
        
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