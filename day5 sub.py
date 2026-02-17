weights = [4, 18, 70, -2, 30, 55, 0]

full_name = "ayman shaik"
name_without_space = full_name.replace(" ", "")
L = len(name_without_space)
PLI = L % 3

very_light = []
normal_load = []
heavy_load = []
overload = []
invalid_entries = []

total_valid = 0

for w in weights:
    if w < 0:
        invalid_entries.append(w)
    elif w >= 0 and w <= 5:
        very_light.append(w)
        total_valid += 1
    elif w >= 6 and w <= 25:
        normal_load.append(w)
        total_valid += 1
    elif w >= 26 and w <= 60:
        heavy_load.append(w)
        total_valid += 1
    else:
        overload.append(w)
        total_valid += 1

affected_items = 0

if PLI == 0:
    for item in overload:
        invalid_entries.append(item)
        affected_items += 1
    overload = []
elif PLI == 1:
    affected_items = len(very_light)
    very_light = []
else:
    affected_items = len(very_light) + len(overload)
    very_light = []
    overload = []

print("L value:", L)
print("PLI value:", PLI)

if PLI == 0:
    print("Applied Rule: A")
elif PLI == 1:
    print("Applied Rule: B")
else:
    print("Applied Rule: C")

print("Very Light:", very_light)
print("Normal Load:", normal_load)
print("Heavy Load:", heavy_load)
print("Overload:", overload)
print("Invalid Entries:", invalid_entries)
print("Total Valid Weights:", total_valid)
print("Affected Items Due to PLI:", affected_items)
