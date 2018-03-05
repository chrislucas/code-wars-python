import re

'''
https://www.codewars.com/kata/515decfd9dcfc23bb6000006/train/python
'''

pattern_ip1 = "(2[0-5]{2})|(1[0-9]{2})|([1-9][0-9])|([0-9])(\.((2[0-5]{2})|(1[0-9]{2})|([1-9][0-9])|([0-9]))){3}"


def is_valid_IP(_str):
    obj_match = re.match(pattern_ip1, _str)
    if obj_match is not None:
        print(obj_match)
        _str_match = _str[obj_match.pos:obj_match.endpos]
        print(_str_match)
    return ''


print(is_valid_IP('12.255.56.1'))
print(is_valid_IP(''))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('123.456.789.0'))
print(is_valid_IP('12.34.56'))
print(is_valid_IP('12.34.56 .1'))
print(is_valid_IP('12.34.56.-1'))
print(is_valid_IP('123.045.067.089'))
print(is_valid_IP('127.1.1.0'))
print(is_valid_IP('0.0.0.0'))
print(is_valid_IP('0.34.82.53'))
print(is_valid_IP('192.168.1.300'))

if __name__ == '__main__':
    pass
