import pandas as pd
import random
from faker import Faker
import os


fake = Faker()

campaigns = []

channels = [
    "Google Ads",
    "Facebook Ads",
    "LinkedIn Ads",
    "Email Marketing",
    "Referral Program"
]

campaign_types = [
    "Summer Promotion",
    "Product Launch",
    "Lead Generation",
    "Brand Awareness",
    "Retargeting"
]

for campaign_id in range(1, 21):

    start_date = fake.date_between(
        start_date="-1y",
        end_date="-1m"
    )

    end_date = fake.date_between(
        start_date=start_date,
        end_date="today"
    )

    campaigns.append({
        "campaign_id": campaign_id,
        "campaign_name": f"{random.choice(campaign_types)} {campaign_id}",
        "channel": random.choice(channels),
        "budget": random.randint(10000, 200000),
        "start_date": start_date,
        "end_date": end_date
    })

campaigns_df = pd.DataFrame(campaigns)

# Resolve paths relative to the script location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
campaigns_path = os.path.join(base_dir, "data", "raw", "marketing_campaigns.csv")

# Ensure target directory exists
os.makedirs(os.path.dirname(campaigns_path), exist_ok=True)

campaigns_df.to_csv(
    campaigns_path,
    index=False
)

print(f"{len(campaigns_df)} marketing campaigns generated successfully")