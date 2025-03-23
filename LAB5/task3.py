import re 
with open("PP2/LAB5/row.txt", encoding = "utf-8") as file:
    info = file.read()
z = re.findall("[a-z]_+[a-z]+", info)
print(z)