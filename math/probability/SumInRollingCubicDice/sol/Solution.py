'''
https://www.codewars.com/kata/probabilities-for-sums-in-rolling-cubic-dice/train/python
'''
from builtins import print


def _combination(arr, chosen, s, e, c, p, _sum):
    if c == p:
        acc2 = 0
        for i in range(0, p):
            acc2 += arr[chosen[i]]
            #print("%d " % arr[chosen[i]], end='')
        #print("")
        flag = True
        for a in range(0, len(chosen)-1):
            if chosen[a] - chosen[a+1] != 0:
                flag = False
                break
        if acc2 == _sum:
            if flag:
                return 1
            else:
                acc = 1
                for x in range(len(chosen), 0, -1):
                    acc *= x
                return acc
        return 0
    acc = 0
    for i in range(s, e):
        chosen[c] = i
        acc += _combination(arr, chosen, i, e, c + 1, p, _sum)
    return acc


def combinaroty(arr, _sum, p):
    chosen = [0] * p
    _len = len(arr)
    return _combination(arr, chosen, 0, _len, 0, p, _sum)


def rolldice_sum_prob(_sum, dice_amount):
    # your code here
    a = combinaroty([1, 2, 3, 4, 5, 6], _sum, dice_amount)
    # prob = probability of having the sum value when rolling dice
    return a / (6 ** dice_amount)


#print(rolldice_sum_prob(3, 3))
print(rolldice_sum_prob(11, 2))
print(rolldice_sum_prob(8, 3))
#print(rolldice_sum_prob(8, 2))

if __name__ == '__main__':
    pass
