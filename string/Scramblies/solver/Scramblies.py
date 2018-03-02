'''
https://www.codewars.com/kata/scramblies/train/python
DONE
'''

from string import ascii_lowercase


def solver_v2(s1, s2):
    _dict_s1 = dict()
    for c in s1:
        if c in _dict_s1:
            _dict_s1[c] += 1
        else:
            _dict_s1[c] = 1

    _dict_s2 = dict()
    for c in s2:
        if c in _dict_s2:
            _dict_s2[c] += 1
        else:
            _dict_s2[c] = 1

    acc = 0
    for c in s2:
        if c not in _dict_s1:
            break
        elif _dict_s1[c] >= _dict_s2[c]:
            acc += 1

    return True if acc == len(s2) else False


def scramble(s1, s2):
    # your code here
    _dict = dict((x, False) for x in ascii_lowercase)
    for c in s1:
        _dict[c] = True

    _dict_s1 = dict()
    for c in s1:
        if c in _dict_s1:
            _dict_s1[c] += 1
        else:
            _dict_s1[c] = 1

    _dict_s2 = dict()
    for c in s2:
        if c in _dict_s2:
            _dict_s2[c] += 1
        else:
            _dict_s2[c] = 1

    acc = 0
    for c in s2:
        if _dict[c] and _dict_s1[c] >= _dict_s2[c]:
            acc += 1

    return True if acc == len(s2) else False


print(scramble('rkqodlw', 'world'))
print(solver_v2('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(solver_v2('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(solver_v2('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(solver_v2('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
print(solver_v2('scriptingjava', 'javascript'))

if __name__ == '__main__':
    pass
