import pandas as pd
from faker import Faker
import random
from tqdm import tqdm
import uuid

# To run this script
# pipenv run python __datagen/generator.py

fake = Faker()
#num_records = 2_000_000  # 2 million records
#output_file = "test_data_2mil.csv"
#num_records = 300_000  # 300 thousand records
#output_file = "test_data_300k.csv"

num_records = 100  # num of recs
output_file = "test_data_100.csv"


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

def generate_claims_data():
    return {
        "TimeStamp": fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
        "BINNumber": fake.bothify(text='??####').upper(),
        "ProcessorControlNo": fake.bothify(text='??#########').upper(),
        "NationalProviderID": fake.bothify(text='??############').upper(),
        "ServiceProviderID": fake.bothify(text='??############').upper(),
        "ServiceProviderIDQual": fake.bothify(text='??').upper(),
        "TransactionCode": fake.bothify(text='??').upper(),
        "DateOfService": fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
        "PatientFirstName": fake.first_name(),
        "PatientLastName": fake.last_name(),
        "PatientDOB": fake.date_of_birth(minimum_age=18, maximum_age=90),
        "PatientGender": fake.random_element(elements=('M', 'F')),
        "OtherCoverageCode": fake.bothify(text='??').upper(),
        "PatientStreetAddress": fake.street_address(),
        "PatientCityAddress": fake.city(),
        "PatientState": fake.state_abbr(),
        "PatientZip": fake.zipcode(),
        "PrescriptionRefNo": fake.bothify(text='??#########').upper(),
        "FillNo": fake.bothify(text='??').upper(),
        "ProductServiceIDQual": fake.bothify(text='??').upper(),
        "ProductServiceID": fake.bothify(text='??###############').upper(),
        "PrescriberIDQual": fake.bothify(text='??').upper(),
        "PrescriberID": fake.bothify(text='??###############').upper(),
        "IngredientCostSubmitted": round(random.uniform(10, 120), 2),
        "GrossAmountDue": round(random.uniform(0, 120), 2),
        "UnitOfMeasure": fake.random_element(elements=('EA', 'ML', 'MG', 'G')),
        "QuantityDispensed": random.randint(1, 30),
        "TransactionResponseStatus": fake.random_element(elements=(0, 1)),
        "TotalAmountPaid": round(random.uniform(0, 120), 2),
        "IngredientCostPaid": round(random.uniform(10, 120), 2),
        "PatientPayAmount": round(random.uniform(0, 120), 2),
        "IncentiveAmountPaid": round(random.uniform(0, 120), 2),
        "DispensingFeePaid": round(random.uniform(0, 120), 2),
        "FlatSalesTaxAmountPaid": round(random.uniform(0, 120), 2),
        "PercentageSalesTaxAmountPaid": round(random.uniform(0, 120), 2),
        "OtherAmountPaid": round(random.uniform(0, 120), 2),
        "AmountOfCopayCoinsurance": round(random.uniform(0, 120), 2),
        "AmtAttToProdSelection": round(random.uniform(0, 120), 2),
        "AuthorizationNo": str(uuid.uuid4()),
        "CardholderID": fake.bothify(text='??###############').upper(),
        "GroupNo": fake.bothify(text='??###############').upper(),
        "CompoundCode": fake.random_element(elements=(0, 1)),
        "DaysSupply": fake.random_element(elements=(30, 60, 90)),
        "FacilityCode" : fake.bothify(text='??#######').upper(),
        "CoordinationOfBenefits" : fake.bothify(text='??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789').upper(),
        "DateRxWritten" : fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S"),
        "PrescriptionOriginCode" : fake.random_element(elements=(0, 1)),
        "PrescriberAddress" : fake.street_address(),
        "SubmissionClarificationCode" : fake.bothify(text='??###########').upper(),
        "CostDetermination" : fake.bothify(text='??#####').upper(),
        "UsualAndCustomaryCharge" : round(random.uniform(0, 800), 2),
    }

# Generate the dataset
#data = [generate_data() for _ in tqdm(range(num_records), desc="Generating Records")]
data = [generate_claims_data() for _ in tqdm(range(num_records), desc="Generating Records")]

# Convert to a DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv(output_file, index=False)

print(f"CSV file '{output_file}' with {num_records:,} records created successfully!")
