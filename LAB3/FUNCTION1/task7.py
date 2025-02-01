def has33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
    
n = input("Enter numbers: ")
nlist = list(map(int, n.split()))

print(has33(nlist))