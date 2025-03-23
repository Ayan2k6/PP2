import re
with open("PP2/LAB5/row.txt") as file:
    info = file.read()
print(re.findall(r"[A-Z][^A-Z]*", info))