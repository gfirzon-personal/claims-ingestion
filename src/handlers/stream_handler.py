from services import (StorageService)

def process_csv_chunks(stream):
    # Process each chunk as it arrives
    buffer = ""
    for chunk in stream:
        buffer += chunk.decode('utf-8')
        while '\n' in buffer:
            line, buffer = buffer.split('\n', 1)
            yield line
    if buffer:
        yield buffer 

def process_csv_file(container_name, blob_name):
    storage_service = StorageService()
    line_count = 0
    for line in process_csv_chunks(storage_service.stream_blob_file2(container_name, blob_name)):
        line_count += 1                  
        if line_count % 1000 == 0:
            print(f"Received lines {line_count}")

        process_csv_line(line)
    print(f"Received lines {line_count}")

def process_csv_line(line: str):
    """Process a line of a CSV file"""
    print(f"Processing line: {line}")    

def example(container_name: str, blob_name: str):
    # Process each chunk as it arrives
    for chunk in StorageService().stream_blob_file2(container_name, blob_name):
        #print(chunk.decode('utf-8', errors='ignore'))  # Decode if it's text
        print(f"Received chunk of size {len(chunk)}") 

# if __name__ == "__main__":
#     process_blob_stream("testcontainer", "testfile.txt")        