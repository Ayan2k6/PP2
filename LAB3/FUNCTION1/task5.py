from itertools import permutations

def print_perm():
    user_input = input("Enter a string: ")
    list_perm = permutations(user_input)

    for x in list_perm:
        print("".join(x))

print_perm()