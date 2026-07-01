import pandas as pd
import os

# Resolve paths relative to the script location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
subscriptions_path = os.path.join(base_dir, "data", "raw", "subscriptions.csv")

# Load subscriptions
subscriptions = pd.read_csv(subscriptions_path)

revenue_records = []
revenue_id = 1

for _, sub in subscriptions.iterrows():

    start_date = pd.to_datetime(sub["start_date"])

    # Determine last payment date
    if pd.isna(sub["end_date"]):
        end_date = pd.Timestamp.today()
    else:
        end_date = pd.to_datetime(sub["end_date"])

    # Generate monthly payments
    payment_dates = pd.date_range(
        start=start_date,
        end=end_date,
        freq="MS"
    )

    for payment_date in payment_dates:

        revenue_records.append({
            "revenue_id": revenue_id,
            "customer_id": sub["customer_id"],
            "subscription_id": sub["subscription_id"],
            "payment_date": payment_date.date(),
            "amount": sub["monthly_price"]
        })

        revenue_id += 1

revenue_df = pd.DataFrame(revenue_records)

revenue_path = os.path.join(base_dir, "data", "raw", "revenue.csv")
revenue_df.to_csv(
    revenue_path,
    index=False
)

print(f"{len(revenue_df)} revenue records generated successfully")