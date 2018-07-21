def power_set(n):
    for i in range(0, 1<< n):
        for j in range(n-1, -1, -1):
            print("%d" % (1 if i & (1 << j) > 0 else 0), end="")
        print("")
    return


def combination(arr):
    n = len(arr)
    for i in range(0, 1<<n):
        flag = False
        for j in range(0, n):
            if i & (1 << j) > 0:
                flag = True
                print("%s " % arr[j], end="")
        if flag:
            print("")
    return


combination([1,2,3,4,5])

if __name__ == '__main__':
    pass
