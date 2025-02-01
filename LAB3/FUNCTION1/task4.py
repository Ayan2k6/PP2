def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    numbers = list(map(int, numbers.split()))
    return [x for x in numbers if isPrime(x)]
numbers = input()
print(filter_prime(numbers))