# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python
# https://mathschallenge.net/library/number/sum_of_cubes
#DONE

from math import log10, sqrt, floor

def log(logt, base):
    return log10(logt) / log10(base)

'''
 (n^2+n) // 2 ^ 2
'''
def test(n):
    acc = 0
    for i in range(1, n+1):
        acc += i ** 3
        print(i, find_nb(acc), acc, ((i*i+i)//2) ** 2)


'''
Usando equacao de 2 grau
'''


def find_nb(volume):
    c = -sqrt(volume) * 2
    delta = floor(sqrt(1-4*c))
    if delta*delta != 1-4*c:
        return -1
    else :
        p = int(delta // 2)
        return -1 if (p*p+p)//2*(p*p+p)//2 != volume else p

#test(1000)
print(find_nb(3153))
print(find_nb(450010))
print(find_nb(1071225))
print(find_nb(91716553919377))
print(find_nb(24723578342962))
print("\n")
print(find_nb(4183059834009))
print(find_nb(135440716410000))
print(find_nb(40539911473216))
print(find_nb(26825883955641))
if __name__ == '__main__':
    pass