def solve(numheads, numlegs):
    # Let x be the number of chickens and y be the number of rabbits
    # We have two equations:
    # x + y = numheads  (total number of animals)
    # 2x + 4y = numlegs (total number of legs)  --> x + 2y = numlegs / 2

    # Solving for x and y:
    y = (numlegs // 2) - numheads
    x = numheads - y

    return f"We have {x} chickens and {y} rabbits"
print ("numer of heads: ")
numheads = int(input())
print ("numer of legs: ")
numlegs = int(input())
print(solve(numheads, numlegs))
