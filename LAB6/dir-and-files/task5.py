f = open("PP2/LAB6/dir-and-files/just.text", "a")
s = list(map(str, input().split()))
for i in s:
    f.write(i + "\n")
f.close
f = open("PP2/LAB6/dir-and-files/just.text", "r")
f.read()
f.close()