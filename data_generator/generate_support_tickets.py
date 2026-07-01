import pandas as pd
import random
from faker import Faker
from datetime import timedelta
import os

fake = Faker()

# Resolve paths relative to the script location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
customers_path = os.path.join(base_dir, "data", "raw", "customers.csv")

customers = pd.read_csv(customers_path)

tickets = []
ticket_id = 1

issue_categories = [
    "Billing",
    "Login Issue",
    "Bug Report",
    "Feature Request",
    "Account Management"
]

priorities = ["Low", "Medium", "High", "Critical"]

statuses = ["Resolved", "Open"]

# Create around 3000 tickets

for _ in range(3000):

    customer = customers.sample(1).iloc[0]

    created_date = fake.date_between(
        start_date="-1y",
        end_date="today"
    )

    status = random.choices(
        statuses,
        weights=[85, 15]
    )[0]

    if status == "Resolved":
        resolved_date = created_date + timedelta(
            days=random.randint(1, 10)
        )
    else:
        resolved_date = "2099-12-31"

    tickets.append({
        "ticket_id": ticket_id,
        "customer_id": customer["customer_id"],
        "issue_category": random.choice(issue_categories),
        "priority": random.choice(priorities),
        "status": status,
        "created_date": created_date,
        "resolved_date": resolved_date
    })

    ticket_id += 1

tickets_df = pd.DataFrame(tickets)

tickets_path = os.path.join(base_dir, "data", "raw", "support_tickets.csv")
# Ensure target directory exists
os.makedirs(os.path.dirname(tickets_path), exist_ok=True)

tickets_df.to_csv(
    tickets_path,
    index=False
)

print(
    f"{len(tickets_df)} support tickets generated successfully"
)