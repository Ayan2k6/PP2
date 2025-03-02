with open('PP2/LAB6/dir-and-files/info1.txt', 'r') as f1, open('PP2/LAB6/dir-and-files/info2.txt', 'a') as f2:
    for i in f1:
        f2.write(i)