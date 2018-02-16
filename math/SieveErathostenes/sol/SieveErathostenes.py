# https://www.codewars.com/kata/sieve-of-eratosthenes-1/python
# https://www.codewars.com/kata/master-your-primes-sieve-with-memoization
# DONE

def sieve_of_eratosthenes(n):
    n += 1
    list = []
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
            list.append(i)

    return list


_list = sieve_of_eratosthenes(97)

print(_list)
print(len(_list))

if __name__ == "__main__":
    pass
