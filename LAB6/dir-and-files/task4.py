import os
with open("PP2/LAB5/row.txt", "r") as f:
    d = f.read()
print(len(list(d.split("\n"))))