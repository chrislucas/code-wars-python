'''
https://www.codewars.com/kata/596d34df24a04ee1e3000a25/train/python
'''
def countOne(left, right):
    # Your code here!
    return 0


'''
quando subtraimos 1 de um numero n, todos os bits
da direita ate o bit mais significativo a direita sao invertidos
exemplo 
10 = 1010. 10-1=9=1001
9 = 1001. 9-1=8=1000

n & (n-1) transforma o bit menos significativo de n em 0
se colocarmos isso num loop podemos otimizar a contagem de bits signiticativos
'''
def count_ones(n):
    acc = 0
    while n > 0:
        n &= (n - 1)
        acc += 1
    return acc


def is_power_of_2(n):
    return n & (n - 1) == 0 and n > 0


def test():
    for x in range(0, 255):
        #print("x: %d nbits: %d" % (x, 1 if is_power_of_2(x) else count_ones(x)))
        print("x: %d nbits: %d" % (x, count_ones(x)))


test()

if __name__ == '__main__':
    pass
