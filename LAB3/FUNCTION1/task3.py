def myfunc(numheads, numlegs):
    # Let x be the number of chickens and y be the number of rabbits
    # We have two equations:
    # x + y = numheads  (total number of animals)
    # 2x + 4y = numlegs (total number of legs)

    # Solving for x and y:
    x = numlegs - 2 * y
    y = numheads - x

    return x,y
print ("numer of heads: ")
y = int(input())
print ("numer of legs: ")
x = int(input())
print(myfunc(numheads, numlegs))
