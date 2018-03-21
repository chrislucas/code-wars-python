'''
https://www.codewars.com/kata/josephus-survivor/train/python
DONE
'''


def rec_approach(n, k):
    if n == 1:
        return 1
    acc = rec_approach(n - 1, k)
    return (acc + (k - 1)) % n + 1


def it_approach(n, k):
    acc = 1
    for i in range(2, n + 1):
        acc = (acc + (k - 1)) % i + 1
    return acc


def josephus_survivor(n, k):
    # your code here
    return it_approach(n, k)


print(josephus_survivor(100, 1))
print(josephus_survivor(7, 3))
print(josephus_survivor(11, 19))
print(josephus_survivor(1, 300))
print(josephus_survivor(14, 2))

if __name__ == '__main__':
    pass
