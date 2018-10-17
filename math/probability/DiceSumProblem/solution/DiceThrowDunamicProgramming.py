'''
https://www.geeksforgeeks.org/dice-throw-dp-30/
'''


def f(faces, dices, acc):
    if dices == 0:
        return 1
    ans = 0
    for i in range(1, faces):
        ans += f(faces, dices - 1, acc - i)

    return ans


print(f(4, 2, 1))
print(f(2, 2, 3))
print(f(6, 3, 8))
print(f(4, 2, 5))
print(f(4, 3, 5))



if __name__ == '__main__':
    pass
