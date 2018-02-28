'''
https://www.codewars.com/kata/maximum-subarray-sum/discuss/python
DONE
'''
def maxSequence(arr):
    maxCur, maxEnd = arr[0] if len(arr) > 0 else 0, 0
    for i in range(1, len(arr)):
        maxCur = arr[i] if arr[i] > arr[i] + maxCur else arr[i] + maxCur
        maxEnd = maxEnd if maxEnd > maxCur else maxCur
    return maxEnd


print(maxSequence([]))
print(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maxSequence([-2, -3, 4, -1, -2, 1, 5, -3]))
print(maxSequence([-2, -3, -4, -1, -2, -1, -5, -3]))


if __name__ == '__main__':
    pass