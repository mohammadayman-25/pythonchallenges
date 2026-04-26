import random
import math
import numpy as np
import pandas as pd


def generate_data(n=18):
    data = []
    for i in range(1, n + 1):
        data.append({
            "zone": i,
            "traffic": random.randint(0, 100),
            "air_quality": random.randint(0, 300),
            "energy": random.randint(0, 500)
        })

    data.append({"zone": 99, "traffic": 0, "air_quality": 250, "energy": 450})
    data.append({"zone": 100, "traffic": 10, "air_quality": 50, "energy": 50})
    data.append({"zone": 101, "traffic": 40, "air_quality": 120, "energy": 450})

    return data


def classify(d):
    if d["air_quality"] > 200 or d["traffic"] > 80:
        return "High Risk"
    elif d["energy"] > 400:
        return "Energy Critical"
    elif d["traffic"] < 30 and d["air_quality"] < 100:
        return "Safe Zone"
    return "Moderate"


def risk(d):
    return (d["traffic"] * 0.4 +
            d["air_quality"] * 0.4 +
            d["energy"] * 0.2)


def sort_data(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1):
            if data[j]["traffic"] > data[j + 1]["traffic"]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def patterns(df):
    threshold = df["risk_score"].mean()

    rising = df[(df["risk_score"] > threshold) & (df["air_quality"].diff() > 0)]

    var = np.var(df["traffic"])
    stability = "Stable" if var < 500 else "Unstable"

    clusters = []
    for i in range(len(df) - 1):
        if df.loc[i, "risk_score"] > threshold and df.loc[i + 1, "risk_score"] > threshold:
            clusters.append((df.loc[i, "zone"], df.loc[i + 1, "zone"]))

    return rising, stability, clusters


roll_no_last_digit = 7

data = generate_data()

for d in data:
    d["category"] = classify(d)
    d["risk_score"] = risk(d)

if roll_no_last_digit % 3 == 0:
    random.shuffle(data)
else:
    data = sort_data(data)


df = pd.DataFrame(data)

df["risk_transformed"] = df["risk_score"].apply(lambda x: math.sqrt(x))

top3 = sorted(data, key=lambda x: x["risk_score"], reverse=True)[:3]

rising, stability, clusters = patterns(df)

max_r = df["risk_score"].max()
avg_r = df["risk_score"].mean()
min_r = df["risk_score"].min()

risk_tuple = (max_r, avg_r, min_r)

if max_r > 350:
    decision = "Critical Emergency"
elif avg_r > 250:
    decision = "High Alert"
elif avg_r > 150:
    decision = "Moderate Risk"
else:
    decision = "City Stable"


print("\nDataFrame:\n", df)

print("\nZones:\n", df[["zone", "category"]])

print("\nTop 3 Risk Zones:")
for z in top3:
    print(z)

print("\nRisk Tuple:", risk_tuple)

print("\nStability:", stability)

print("\nClusters:", clusters)

print("\nFinal Decision:", decision)