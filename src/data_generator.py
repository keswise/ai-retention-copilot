from faker import Faker
import pandas as pd
import random

fake = Faker()

users = []

for i in range(10000):

    sessions = random.randint(1, 100)

    last_login_days = random.randint(1, 90)

    revenue = random.randint(0, 5000)

    churn = 1 if last_login_days > 45 else 0

    users.append({
        "user_id": i,
        "sessions": sessions,
        "last_login_days": last_login_days,
        "revenue": revenue,
        "country": fake.country(),
        "churn": churn
    })

df = pd.DataFrame(users)

df.to_csv("data/users.csv", index=False)

print("Dataset Generated")