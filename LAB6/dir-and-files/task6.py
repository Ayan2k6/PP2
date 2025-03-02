from string import ascii_uppercase
import os
for i in ascii_uppercase:
    fn = i + ".txt"
    with open(fn, "w") as file:
        file.write(f"{i} file")