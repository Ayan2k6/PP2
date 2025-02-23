import re
with open("LAB5/row.txt") as file:
    info = file.read()
z = re.findall("a.*b", info)
print(z)
