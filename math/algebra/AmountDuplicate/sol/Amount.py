'''
https://www.codewars.com/kata/unknown-amount-of-duplicates-one-missing-number/train/python
'''

'''
TIME OUT
'''
def approachV1(arr):
    _map = {}
    repeated = []
    possible_missing = []
    maxValue, minValue = arr[0], arr[0]
    for i in arr:
        if i > maxValue:
            maxValue = i
        if i < minValue:
            minValue = i
        if i not in _map:
            _map[i] = 1
        else:
            _map[i] += 1
            if i not in repeated:
                repeated.append(i)

    for i in range(minValue, maxValue + 1):
        if i not in arr:
            possible_missing.append(i)
    repeated.sort()
    return [possible_missing[0], repeated]

'''
TIME OUT
'''
def approachV2(arr):
    _map = {}
    repeated = []
    maxValue, minValue = arr[0], arr[0]
    acc = 0
    for i in arr:
        if i > maxValue:
            maxValue = i
        if i < minValue:
            minValue = i
        if i not in _map:
            _map[i] = 1
            acc += i
        else:
            _map[i] += 1
            if i not in repeated:
                repeated.append(i)

    # quantos numeros temos na sequencia entre min e max inclusive ?
    t = maxValue - minValue + 1
    # soma dos numeros entre min e max inclusive - usando a formula para soma de termos de uma P.A
    summation = t * (maxValue + minValue) // 2
    repeated.sort()
    return [summation - acc, repeated]

'''
ACCEPTED
'''
def approachV3(arr):
    _map = {}
    maxValue, minValue = arr[0], arr[0]
    acc = 0
    for i in arr:
        if i > maxValue:
            maxValue = i
        if i < minValue:
            minValue = i
        if i not in _map:
            _map[i] = 1
            acc += i
        else:
            _map[i] += 1

    # quantos numeros temos na sequencia entre min e max inclusive ?
    t = maxValue - minValue + 1
    # soma dos numeros entre min e max inclusive - usando a formula para soma de termos de uma P.A
    summation = t * (maxValue + minValue) // 2

    flags = [False] * (maxValue - minValue + 1)
    for k, v in _map.items():
        if v > 1:
            flags[k - minValue] = True
    repeated = []
    for i in range(0, len(flags)):
        if flags[i]:
            repeated.append(i + minValue)
    return [summation - acc, repeated]

def find_dups_miss(arr):
    # your code here
    return approachV2(arr)


print(find_dups_miss([500,501,503,503]))
print(find_dups_miss([10,10,9,8,9,6,1,2,4,3,2,5,5,3]))
print(find_dups_miss([10,9,8,9,6,1,2,4,3,2,5,5,3]))
print(find_dups_miss([20,19,6,9,7,17,16,17,12,5,6,8,9,10,14,13,11,14,15,19]))
print(find_dups_miss([24,25,34,40,38,26,33,29,50,31,33,56,35,36,53,49,57,27,37,40,48,44,32,35,45,52,43,47,26,51,55,28,41,42,46,51,25,30,44,54]))

if __name__ == '__main__':
    pass