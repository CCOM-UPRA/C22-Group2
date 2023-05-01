import json

# Load JSON data into a dictionary
with open('JSONfiles/products.json') as f:
    data = json.load(f)

# Access keys and sub-keys and put them into a Python list
my_list = []
for key in data.keys():
    item = [key]
    for sub_key in data[key].keys():
        item.append(data[key][sub_key])
    my_list.append(item)

# Print the list
print(my_list)
