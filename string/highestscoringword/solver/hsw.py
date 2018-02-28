'''
https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python
DONE
'''

from string import ascii_lowercase as alphabet


def high(x):
    # Code here
    data = {}
    alpha = list(alphabet)
    for idx in range(0, len(alpha)):
        data[alpha[idx]] = idx + 1

    _list = x.split(' ')
    _max = 0
    _word = ""
    for _str in _list:
        _acc = sum([data[c] for c in _str])
        if _max < _acc:
            _max = _acc
            _word = _str

    return _word


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))

if __name__ == '__main__':
    pass
