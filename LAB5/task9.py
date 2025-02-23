import re
with open("LAB5/row.txt") as file:
    info = file.read()
print(re.sub(r"([A-Z])", r" \1", info))