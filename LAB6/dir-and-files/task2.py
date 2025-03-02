import os 
def check(p):
    if os.access(p, os.F_OK):
        print("Path exists")
    else:
        print("Path doesn`t exist")
    if os.access(p, os.R_OK):
        print("Path is readble")
    else:
        print("Path isn`t readble")
    if  os.access(p, os.W_OK):    
        print("Path is writable")
    else:
        print("'Path isn`t writable")
    if  os.access(p, os.X_OK): 
        print("Path is executable:") 
    else:
        print("Path isnt executable:")
p = r"C:\Users\user\Desktop\CODES\PP2"
check(p)