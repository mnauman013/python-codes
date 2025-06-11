x = int(input("Enter a number to check if it is prime: "))

def check_prime(is_prime):
    if is_prime:
        print("The number is prime")
    else:
        print("The number is not prime")

#method 1
def prime_1(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
check_prime(prime_1(x))

#method 2
def prime_2(x):
    if x <= 1:
        return False
    if x <= 3:
        return False
    if x % 2 == 0 or x % 3 == 0:
        return False
    i  = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
check_prime(prime_2(x))

#method 3
def prime_3(x, divisor = 2):
    if x <= 1:
        return False
    if divisor * divisor > x:
        return True
    if x % divisor == 0:
        return False
    return prime_3(x, divisor + 1)
check_prime(prime_3(x))

#method 4
prime_4 = all(map(lambda i: x % i != 0, range(2, int(x**0.5) + 1))) if x > 1 else False
check_prime(prime_4)

#method 5, To get prime numbers upto n by using Sieve of Eratosthenes
def sieve_method(y):
    if y <= 1:
        return []
    sieve = [True] * (y + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(y**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, y + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]
print("List of prime numbers up to n: ", sieve_method(x))
