import re 
with open("PP2/LAB5/row.txt", encoding = "utf-8") as file:
    info = file.read()
zz = re.sub(r"_",'', info)
print(zz)