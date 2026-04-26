import random
import math
import copy
import numpy as np
import pandas as pd


# ---------- Function 1 ----------
# Create random data for 15 zones
def create_zones(total=15):
    zones = []

    for i in range(1, total + 1):
        zone_data = {
            "zone": i,
            "metrics": {
                "traffic": random.randint(50, 150),
                "pollution": random.randint(20, 100),
                "energy": random.randint(40, 120)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }

        zones.append(zone_data)

    return zones


# ---------- Function 2 ----------
# Personalization rule
def apply_personal_rule(data, last_digit):

    # EVEN -> reverse dataset
    if last_digit % 2 == 0:
        data.reverse()

    # ODD -> rotate by 3
    else:
        data = data[3:] + data[:3]

    return data


# ---------- Function 3 ----------
# Custom risk formula
def custom_risk_score(traffic, pollution, energy):
    total = traffic + pollution + energy
    return math.log(total)


# ---------- Function 4 ----------
# Manual correlation (without using .corr())
def calculate_correlation(x, y):

    mean_x = np.mean(x)
    mean_y = np.mean(y)

    numerator = np.sum((x - mean_x) * (y - mean_y))

    denominator = math.sqrt(
        np.sum((x - mean_x) ** 2) *
        np.sum((y - mean_y) ** 2)
    )

    if denominator == 0:
        return 0

    return numerator / denominator


# ---------- Function 5 ----------
# Detect consecutive risky zones
def find_clusters(zone_list):

    clusters = []
    current = []

    for zone in zone_list:

        if len(current) == 0:
            current.append(zone)

        elif zone == current[-1] + 1:
            current.append(zone)

        else:
            if len(current) > 1:
                clusters.append(current)

            current = [zone]

    if len(current) > 1:
        clusters.append(current)

    return clusters


# ---------- Function 6 ----------
# Final system status
def system_status(corruption, risky_count):

    if corruption and risky_count >= 6:
        return "Critical Failure"

    elif corruption:
        return "High Corruption Risk"

    elif risky_count >= 4:
        return "Moderate Risk"

    else:
        return "System Stable"


# ---------------- MAIN PROGRAM ----------------

digit = int(input("Enter last digit of Register Number: "))

# Step 1
original_data = create_zones(15)

# Apply personalization
original_data = apply_personal_rule(original_data, digit)

print("\n----- BEFORE COPY -----")
for item in original_data[:2]:
    print(item)


# Step 2 Copies
assignment_copy = original_data
shallow_copy = copy.copy(original_data)
deep_copy = copy.deepcopy(original_data)


# Step 3 Mutation

# Modify shallow copy
shallow_copy[0]["metrics"]["traffic"] += 40
shallow_copy[0]["history"].append(999)

# Modify deep copy
deep_copy[1]["metrics"]["pollution"] += 25
deep_copy[1]["history"].append(777)


print("\n----- AFTER COPY MODIFICATION -----")
print("Original First Zone:")
print(original_data[0])

print("\nShallow Copy First Zone:")
print(shallow_copy[0])

print("\nDeep Copy Second Zone:")
print(deep_copy[1])


# Hidden corruption check
if original_data[0]["metrics"]["traffic"] == shallow_copy[0]["metrics"]["traffic"]:
    corruption_found = True
else:
    corruption_found = False


# Step 4 Convert to DataFrame
records = []

for item in original_data:

    zone_no = item["zone"]

    traffic = item["metrics"]["traffic"]
    pollution = item["metrics"]["pollution"]
    energy = item["metrics"]["energy"]

    risk = custom_risk_score(traffic, pollution, energy)

    records.append([
        zone_no,
        traffic,
        pollution,
        energy,
        risk
    ])


df = pd.DataFrame(
    records,
    columns=["zone", "traffic", "pollution", "energy", "risk"]
)

print("\n----- DATAFRAME -----")
print(df)


# NumPy Analysis
mean_risk = np.mean(df["risk"])
variance_risk = np.var(df["risk"])
std_risk = np.std(df["risk"])

# Stability Index
stability = 1 / (variance_risk + 0.0001)


# Detect anomalies
anomaly_zones = df[df["risk"] > mean_risk + std_risk]["zone"].tolist()

# High risk zones
risky_zones = df[df["risk"] > mean_risk]["zone"].tolist()

# Cluster detection
clusters = find_clusters(risky_zones)

# Manual correlation
corr_value = calculate_correlation(
    df["traffic"].values,
    df["pollution"].values
)


# Tuple Output
result = (
    round(df["risk"].max(), 3),
    round(df["risk"].min(), 3),
    round(stability, 3)
)


# Final Decision
decision = system_status(corruption_found, len(risky_zones))


# ---------- Final Output ----------

print("\n----- ANALYSIS -----")
print("Mean Risk =", round(mean_risk, 3))
print("Variance =", round(variance_risk, 3))
print("Correlation =", round(corr_value, 3))

print("\nAnomaly Zones =", anomaly_zones)
print("Risky Zones =", risky_zones)
print("Clusters =", clusters)

print("\nTuple Output:")
print(result)

print("\nWhy shallow copy corrupts nested structures?")
print("Because shallow copy creates a new outer list,")
print("but inner dictionaries and lists still refer to same memory.")

print("\nFinal Decision =", decision)