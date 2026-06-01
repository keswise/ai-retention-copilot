import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("data/users.csv")

# Features for segmentation
features = df[
    [
        "sessions",
        "revenue",
        "last_login_days"
    ]
]

# Scale features
scaler = StandardScaler()

features_scaled = scaler.fit_transform(features)

# Train KMeans
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["segment"] = kmeans.fit_predict(features_scaled)

# Analyze clusters
cluster_summary = (
    df.groupby("segment")
      [["sessions", "revenue", "last_login_days"]]
      .mean()
      .round(2)
)

print("\nCluster Characteristics:\n")
print(cluster_summary)

# Assign business names
segment_mapping = {}

for segment in cluster_summary.index:

    revenue = cluster_summary.loc[segment, "revenue"]
    sessions = cluster_summary.loc[segment, "sessions"]
    last_login = cluster_summary.loc[segment, "last_login_days"]

    if revenue > 3500 and sessions > 60:
        segment_mapping[segment] = "High Value"

    elif sessions > 50 and last_login < 30:
        segment_mapping[segment] = "Loyal"

    elif last_login > 60:
        segment_mapping[segment] = "Dormant"

    elif revenue < 1000 and sessions < 20:
        segment_mapping[segment] = "New"

    else:
        segment_mapping[segment] = "At Risk"

# Apply segment names
df["segment_name"] = df["segment"].map(segment_mapping)

print("\nSegment Distribution:\n")
print(df["segment_name"].value_counts())

# Save output
df.to_csv(
    "data/segmented_users.csv",
    index=False
)

print("\nSegmentation Complete")
print("Saved: data/segmented_users.csv")