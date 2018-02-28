'''
https://www.codewars.com/kata/polynomials-ii-coefficients-in-a-list/train/python
DONE
'''


# If polynomial degree == 3
def calc_poly(pol_list, x):
    cpol = []
    q = len(pol_list)-1
    #your code here
    acc, idx2 = 0, q
    for idx in range(q, -1, -1):
        coef = pol_list[q-idx]
        if coef is not 0:
            acc += coef * (x ** idx)
            copy_coef = coef if coef > 0 else -coef
            if idx > 1:
                pol = "{0}*x^{1}".format(copy_coef, idx) if copy_coef > 1 or copy_coef < 0 else "x^{0}".format(idx)
            elif idx == 1:
                pol = "{0}*x".format(copy_coef) if copy_coef > 1 or copy_coef < 0 else "x"
            else:
                pol = "{0}".format(copy_coef)

            # adicionar sinal positivo a esquerda
            if idx2 < q:
                if coef > 0:
                    pol = " + {0}".format(pol)
                else:
                    pol = " - {0}".format(pol)
            # a nao ser que o primeiro coeficiente valido for negativo
            elif coef < 0:
                pol = "-{0}".format(pol)
            cpol.append(pol)
            idx2 -= 1

    return "For {0} with x = {1} the value is {2}".format(''.join(cpol), x, acc)


print(calc_poly([17, 2, 1, -33], 36))
print(calc_poly([1, -18, 35, 79], -42))
print(calc_poly([0, 5, 4], -58))
print(calc_poly([6, 3, 5, -4], 4))
print(calc_poly([2, 0, 5, -6, 4, 0], 2))
print(calc_poly([-1, -6, 28, 79], 35))

if __name__ == '__main__':
    pass