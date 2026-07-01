import pandas as pd
import random
import os

# Resolve paths relative to the script location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
customers_path = os.path.join(base_dir, "data", "raw", "customers.csv")

customers = pd.read_csv(customers_path)

usage_records = []
usage_id = 1

features = [
    "Dashboard",
    "Analytics",
    "Reports",
    "AI Assistant",
    "Export Data",
    "Automation",
    "Forecasting"
]

# Generate ~50,000 usage events

for _ in range(50000):

    customer = customers.sample(1).iloc[0]

    usage_records.append({
        "usage_id": usage_id,
        "customer_id": customer["customer_id"],
        "usage_date": pd.Timestamp.today().normalize()
                     - pd.Timedelta(days=random.randint(0, 365)),
        "login_count": random.randint(1, 10),
        "session_duration_minutes": random.randint(5, 180),
        "feature_used": random.choice(features)
    })

    usage_id += 1

usage_df = pd.DataFrame(usage_records)

usage_path = os.path.join(base_dir, "data", "raw", "product_usage.csv")
# Ensure target directory exists
os.makedirs(os.path.dirname(usage_path), exist_ok=True)

usage_df.to_csv(
    usage_path,
    index=False
)

print(
    f"{len(usage_df)} product usage records generated successfully"
)