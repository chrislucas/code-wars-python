# https://www.codewars.com/kata/master-your-primes-sieve-with-memoization/train/python


from math import sqrt

primes = []

def sieve_of_eratosthenes(n):
    n += 1
    flags = [True] * n
    flags[0], flags[1] = (False, False)
    i = 2
    while i * i <= n:
        if flags[i]:
            j = i * i
            while j < n:
                flags[j] = False
                j += i
        i += 1
    for i in range(0, len(flags)):
        if flags[i]:
            primes.append(i)
    return primes


def contains(array, value):
    for i in array:
        if i == value:
            return True
    return False


def is_prime(n):
    if contains(primes, n):
        return True
    elif (n > 7 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0)) or n < 2:
        return False
    for i in range(7, int(sqrt(n)) + 1):
        if (n % i) == 0:
            return False

    last_prime = primes[len(primes)-1]
    for i in range(last_prime+1, n):
        flag = True
        for j in range(2, int(sqrt(i)) + 1):
            if (i % j) == 0:
                flag = False
                break
        if flag:
            primes.append(i)
    primes.append(n)
    return True


'''
for i in primes:
    print(is_prime(i))
'''

sieve_of_eratosthenes(11)
'''
print(is_prime(1))
print(is_prime(2))
print(is_prime(5))
print(is_prime(143))
print(abs(len(primes)-5) < 3)
print(is_prime(-1))
print(is_prime(29))
print(is_prime(53))
print(is_prime(529))
print(abs(len(primes)-9) < 3)
'''
print(is_prime(289183589))
print(is_prime(75647596379))

print(is_prime(2))
print(is_prime(41299588913))
print(is_prime(91313))

# print(int(sqrt(204701004143)))


print(primes)

if __name__ == "__main__":
    pass
