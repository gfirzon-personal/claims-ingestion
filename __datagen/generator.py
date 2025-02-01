import pandas as pd
from faker import Faker
import random
from tqdm import tqdm
import uuid

# pipenv run python __datagen/generator.py

fake = Faker()
num_records = 2_000_000  # 2 million records
output_file = "test_data.csv"

# Define the structure of your data
def generate_data():
    return {
        #"id": random.randint(1000, 9999),
        "id": str(uuid.uuid4()),  # Generate a GUID
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address().replace("\n", ", "),
        "phone": fake.phone_number(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90),
        "balance": round(random.uniform(1000, 100000), 2),
        "created_at": fake.date_time_this_decade(),
    }

# Generate the dataset
data = [generate_data() for _ in tqdm(range(num_records), desc="Generating Records")]

# Convert to a DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print(f"CSV file '{output_file}' with {num_records} records created successfully!")
