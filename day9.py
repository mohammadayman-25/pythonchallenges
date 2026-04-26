import copy

# Enter your roll number here
roll_number = 24


# Function 1: Create original data
def generate_data():
    users = [
        {
            "id": 1,
            "data": {
                "files": ["a.txt", "b.txt"],
                "usage": 500
            }
        },
        {
            "id": 2,
            "data": {
                "files": ["c.txt"],
                "usage": 300
            }
        }
    ]
    return users


# Function 2: Make different copies
def replicate_data(users):
    assignment_version = users
    shallow_version = copy.copy(users)
    deep_version = copy.deepcopy(users)

    return assignment_version, shallow_version, deep_version


# Function 3: Modify copied data
def modify_data(copied_users, roll_no):

    # If roll number is even -> add file
    if roll_no % 2 == 0:
        copied_users[0]["data"]["files"].append("new_file.txt")

    # If roll number is odd -> remove file
    else:
        if len(copied_users[0]["data"]["files"]) > 0:
            copied_users[0]["data"]["files"].pop()

    # Change usage
    copied_users[0]["data"]["usage"] = 999

    # Remove file from second user
    if "c.txt" in copied_users[1]["data"]["files"]:
        copied_users[1]["data"]["files"].remove("c.txt")


# Function 4: Check integrity
def check_integrity(original, shallow, deep):

    leakage_count = 0
    safe_count = 0

    # Check if original changed
    for i in range(len(original)):
        if original[i]["data"] == shallow[i]["data"]:
            leakage_count += 1

    # Check deep copy safety
    for i in range(len(original)):
        if original[i]["data"] != deep[i]["data"]:
            safe_count += 1

    # Find common files using set
    original_files = set()
    modified_files = set()

    for user in original:
        for file in user["data"]["files"]:
            original_files.add(file)

    for user in shallow:
        for file in user["data"]["files"]:
            modified_files.add(file)

    common_files = original_files.intersection(modified_files)

    report = {
        "Data Leakage": leakage_count,
        "Safe Deep Copy": safe_count,
        "Common Files": common_files,
        "Mutation Depth": "Inner nested data changed"
    }

    result = (leakage_count, safe_count, len(common_files))

    return report, result


# ---------------- MAIN PROGRAM ----------------

# Step 1: Create original data
original_users = generate_data()

print("===== BEFORE CHANGES =====")
print("Original Data:")
print(original_users)

# Step 2: Create copies
assignment_copy, shallow_copy, deep_copy = replicate_data(original_users)

# Step 3: Modify shallow copy
modify_data(shallow_copy, roll_number)

print("\n===== AFTER CHANGES =====")

print("\nOriginal Data:")
print(original_users)

print("\nAssignment Copy:")
print(assignment_copy)

print("\nShallow Copy:")
print(shallow_copy)

print("\nDeep Copy:")
print(deep_copy)

# Step 4: Check integrity
report, final_result = check_integrity(original_users, shallow_copy, deep_copy)

print("\n===== INTEGRITY REPORT =====")
for key, value in report.items():
    print(key, ":", value)

print("\nTuple Output:")
print(final_result)

# Explanation
print("\n===== EXPLANATION =====")
print("Assignment copy uses same memory as original.")
print("Shallow copy creates new outer list only.")
print("Inner dictionaries and lists are shared.")
print("So changing inner list also changes original.")
print("Deep copy creates full separate data.")
print("That is why deep copy stays safe.")
