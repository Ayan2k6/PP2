import re 
with open("PP2/LAB5/row.txt", encoding = "utf-8") as file:
    info = file.read()
z = re.findall("ab{2,3}", info)
print(z)