def myfunc(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = float(input("Enter your grams: "))
print("You have" ,myfunc(grams))
