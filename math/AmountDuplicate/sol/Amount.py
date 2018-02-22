'''
https://www.codewars.com/kata/unknown-amount-of-duplicates-one-missing-number/train/python
'''

def find_min(arr):
    min = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min :
            min = arr[i]
    return min

'''
    for i in range(0, len(possible_missing)):
        flag = False
        for j in arr:
            if possible_missing[i] == j:
                flag = True
                break
        if flag:
            del possible_missing[i]
'''

def approachV1(arr):
    arr.sort()
    repeated = []
    possible_missing = []
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i+1] and arr[i] not in repeated:
            repeated.append(arr[i+1])




    return [possible_missing, repeated]


def find_dups_miss(arr):
    # your code here
    return approachV1(arr)


print(find_dups_miss([10,9,8,9,6,1,2,4,3,2,5,5,3]))

if __name__ == '__main__':
    pass