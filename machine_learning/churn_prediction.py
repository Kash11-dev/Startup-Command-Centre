import os

os.makedirs("predictions", exist_ok=True)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

customers = pd.read_csv("customers.csv")
subscriptions = pd.read_csv("subscriptions.csv")
usage = pd.read_csv("product_usage.csv")
revenue = pd.read_csv("revenue.csv")

df = customers.merge(
    subscriptions,
    on="customer_id",
    how="left"
)

df = df.merge(
    usage,
    on="customer_id",
    how="left"
)

df = df.merge(
    revenue,
    on="customer_id",
    how="left"
)

df["churn"] = (
    df["status"] == "Cancelled"
).astype(int)


for col in df.columns:
    if df[col].dtype == "object" or str(df[col].dtype) == "string":
        df[col] = df[col].fillna("Unknown")
    else:
        df[col] = df[col].fillna(0)

for col in ["country", "industry", "plan_name", "feature_used"]:
    df[col] = LabelEncoder().fit_transform(df[col].astype(str))

#Train Model
features = [
    "login_count",
    "session_duration_minutes",
    "monthly_price",
    "amount",
    "country",
    "industry",
    "plan_name",
    "feature_used"
]

X = df[features]
y = df["churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

#generate predictions 
df["churn_probability"] = model.predict_proba(X)[:, 1]
df["predicted_churn"] = (df["churn_probability"] >= 0.70).astype(int)
df["revenue_at_risk"] = df["predicted_churn"] * df["amount"]

# save predictions 
df[[
    "customer_id",
    "churn_probability",
    "predicted_churn",
    "revenue_at_risk"
]].to_csv(
    "predictions/churn_predictions.csv",
    index=False
)

pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).to_csv(
    "predictions/feature_importance.csv",
    index=False
)




