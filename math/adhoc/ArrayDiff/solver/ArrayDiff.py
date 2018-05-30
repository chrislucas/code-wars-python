def array_diff(a, b):
    #your code here
    strA = "[" + ",".join([str(i) for i in a]) + "]"
    strB = "[" + ",".join([str(i) for i in b]) + "]"
    strC = "[" + ",".join([str(i) for i in a if i not in b]) + "]"
    return "a was %s, b was %s, expected %s" % (strA, strB, strC)


print(array_diff([1, 2], [1]))
print(array_diff([1, 2, 2], [1]))
print(array_diff([1, 2, 2], []))
print(array_diff([], [1,2]))

if __name__ == '__main__':
    pass