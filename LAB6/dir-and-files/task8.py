import os
p = r"C:\Users\user\Desktop\CODES\emptyfile"
if not os.access(p, os.F_OK):
    print("Path doesn`t exist")
else:
     print("Path exists")
     os.remove(p)
     print("File has been removed")