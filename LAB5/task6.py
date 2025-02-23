import re 
with open("LAB5/row.txt", encoding = "utf-8") as file:
    info = file.read()
z = re.sub(r"[., ]",':', info)
print(z)