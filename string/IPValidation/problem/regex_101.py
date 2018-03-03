'''
https://www.tutorialspoint.com/python/python_reg_expressions.htm
'''

import re as regex


def test(pattern, _str):
    re_comp = regex.compile(pattern, regex.MULTILINE)
    result = re_comp.match(_str)
    if result is not None:
        print(result)
        print(result.re)


test("[a-zA-Z]{1,}", "absc12321")
test("(\d{1,3}\.){3}", "123.456.789")




if __name__ == '__main__':
    pass