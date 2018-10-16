'''
https://www.geeksforgeeks.org/dice-throw-dp-30/
'''


def f(faces, dices,  acc):

    if dices == 0:
        return 1
    ans = 0
    for i in range(1, faces):
        ans += f(faces, dices-1, acc - i)

    return ans

if __name__ == '__main__':
    pass