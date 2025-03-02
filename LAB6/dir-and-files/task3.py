import os
p = r"C:\Users\user\Desktop\CODES\PP2"
if not os.access(p, os.F_OK):
    print("Past doesn`t exist")
else:
    print("Path exists ")
    print(f"Name of files : {os.path.basename(p)}")
    print(f"name of dir : {os.path.dirname(p)}")