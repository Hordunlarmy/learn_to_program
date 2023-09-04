def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True  # If no divisors are found, the number is prime


def prime_list(max_prime):
    primeToList = []
    for i in range(2, max_prime):
        if (isPrime(i)):
            primeToList.append(i)
    return primeToList


max_prime = int(input("Max Prime: "))
print(prime_list(max_prime))
