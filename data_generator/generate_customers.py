from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

customers = []

industries = [
    "Technology",
    "Finance",
    "Healthcare",
    "Retail",
    "Education"
]

for customer_id in range(1, 10001):

    customers.append({
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "email": fake.unique.email(),
        "company_name": fake.company(),
        "industry": random.choice(industries),
        "country": fake.country(),
        "signup_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    })

df = pd.DataFrame(customers)

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
customers_path = os.path.join(base_dir, "data", "raw", "customers.csv")
df.to_csv(
    customers_path,
    index=False
)

print("10000 customers generated successfully")