'''
https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

Estudar mais sobre heap
'''

import heapq


def dbl_linear(n):
    pq = []
    heapq.heappush(pq, 1)
    for x in range(0, n):
        v = pq[0]
        while len(pq) != 0 and v == pq[0]:
            heapq.heappop(pq)
        heapq.heappush(pq, 2*v+1)
        heapq.heappush(pq, 3*v+1)
    return pq[0]


print(dbl_linear(10))
print(dbl_linear(20))
print(dbl_linear(30))
print(dbl_linear(50))


if __name__ == '__main__':
    pass
