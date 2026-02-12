data = [10, "Python", "", 25, "Loop", 40]
name = "Ayman"
number_list = []
string_list = []

total_numbers = 0
total_strings = 0
for item in data:
    if type(item) == int:
        number_list.append(item)
        total_numbers += 1
    elif type(item) == str and item != "":
        string_list.append(item)
        total_strings += 1

if len(name) % 2 == 0:
    if len(number_list) > 0:
        number_list.pop(0)
    if len(string_list) > 0:
        string_list.pop(0)
else:
    if len(number_list) > 0:
        number_list.pop()
    if len(string_list) > 0:
        string_list.pop()

print("Numbers List:", number_list)
print("Strings List:", string_list)
print("Total Numbers:", total_numbers)
print("Total Strings:", total_strings)
