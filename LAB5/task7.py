import re 
with open("LAB5/row.txt", encoding = "utf-8") as file:
    info = file.read()
zz = re.sub(r"_",'', info)
print(zz)