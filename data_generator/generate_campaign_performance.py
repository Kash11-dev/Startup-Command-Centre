import pandas as pd
import random
import os

# Resolve paths relative to the script location
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
campaigns_path = os.path.join(base_dir, "data", "raw", "marketing_campaigns.csv")

campaigns = pd.read_csv(campaigns_path)

performance_data = []
performance_id = 1

for _, campaign in campaigns.iterrows():

    start_date = pd.to_datetime(campaign["start_date"])
    end_date = pd.to_datetime(campaign["end_date"])

    dates = pd.date_range(start=start_date, end=end_date, freq="D")

    for date in dates:

        impressions = random.randint(1000, 20000)

        ctr = random.uniform(0.01, 0.08)
        clicks = int(impressions * ctr)

        conversion_rate = random.uniform(0.02, 0.15)
        conversions = int(clicks * conversion_rate)

        spend = round(random.uniform(500, 5000), 2)

        performance_data.append({
            "performance_id": performance_id,
            "campaign_id": campaign["campaign_id"],
            "report_date": date.date(),
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
            "spend": spend
        })

        performance_id += 1

performance_df = pd.DataFrame(performance_data)

performance_path = os.path.join(base_dir, "data", "raw", "campaign_performance.csv")
# Ensure target directory exists
os.makedirs(os.path.dirname(performance_path), exist_ok=True)

performance_df.to_csv(
    performance_path,
    index=False
)

print(
    f"{len(performance_df)} campaign performance records generated successfully"
)