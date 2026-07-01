import pandas as pd
import random
from datetime import timedelta
import os

# Resolve paths relative to the script location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
customers_path = os.path.join(base_dir, "data", "raw", "customers.csv")

# Load customers
customers = pd.read_csv(customers_path)

subscriptions = []

plans = {
    "Basic": 499,
    "Pro": 999,
    "Enterprise": 2999
}

subscription_id = 1

for _, customer in customers.iterrows():

    # 90% customers have a subscription
    if random.random() < 0.9:

        plan_name = random.choice(list(plans.keys()))

        start_date = pd.to_datetime(customer["signup_date"])

        # Most subscriptions still active
        status = random.choices(
            ["Active", "Cancelled"],
            weights=[85, 15]
        )[0]
        if status == "Active":
            end_date = "2099-12-31"
        else:
            end_date = start_date + timedelta(
                days=random.randint(30, 365)
            )

        subscriptions.append({
            "subscription_id": subscription_id,
            "customer_id": customer["customer_id"],
            "plan_name": plan_name,
            "monthly_price": plans[plan_name],
            "start_date": start_date.date(),
            "end_date": end_date,
            "status": status
        })

        subscription_id += 1

subscriptions_df = pd.DataFrame(subscriptions)

subscriptions_path = os.path.join(base_dir, "data", "raw", "subscriptions.csv")
subscriptions_df.to_csv(
    subscriptions_path,
    index=False
)

print(f"{len(subscriptions_df)} subscriptions generated successfully")