'''
https://www.codewars.com/kata/roman-numerals-decoder/train/cpp
DONE
'''

from sys import stdin as _in, stdout as _out

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
INDEX = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}

'''
    III = 3
    IV = 4
    MMVIII = 2008
    MDCLXVI = 1666
'''


def solution(_str):
    acc = 0
    last_ch = INDEX[_str[0]]
    idx = 0
    limit = len(_str)
    while idx < limit:
        ch = _str[idx]
        if idx == 0:
            acc += ROMAN[ch]
            '''
            Se o caracter atual representa um numero menor ou igual que o anterior
            basta soma: Exemplo VI, II, XI, XVI
            '''
            idx += 1
        else:
            if idx < limit - 1:
                next_ch = _str[idx + 1]
                if INDEX[ch] < INDEX[last_ch] and INDEX[ch] < INDEX[next_ch]:
                    acc += ROMAN[next_ch] - ROMAN[ch]
                    idx += 2
                elif INDEX[ch] > INDEX[last_ch]:
                    acc = ROMAN[ch] - acc
                    idx += 1
                else:
                    acc += ROMAN[ch]
                    idx += 1
            else:
                if INDEX[ch] <= INDEX[last_ch]:
                    acc += ROMAN[ch]
                else:
                    acc = ROMAN[ch] - acc
                idx += 1
        last_ch = ch
    return acc


'''
https://www.somatematica.com.br/fundam/tabela1.php
'''
'''
print(solution("XLIX"))  # 49
print(solution("XLVIII"))  # 48
print(solution("XLVII"))  # 47
print(solution("XLVI"))  # 46
print(solution("XLV"))  # 45
print(solution("DXXIX"))  # 529
print(solution("I"))
print(solution("II"))
print(solution("III"))
print(solution("IV"))
print(solution("V"))
print(solution("VI"))
print(solution("VII"))
print(solution("IX"))
print(solution("XC"))
print(solution("MMVIII"))

'''

print(solution("CMLXXII"))  # 972
print(solution("CMXCIX"))  # 999
print(solution("MLXVIII"))  # 1068
print(solution("MCCCLXVI"))  # 1366
print(solution("MCDXLIX"))  # 1449
print(solution("MDCCCLXXXVIII"))  # 1888
print(solution("MMXXXIX"))  # 2039

if __name__ == '__main__':
    pass
