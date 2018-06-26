'''
http://www.codewars.com/kata/rgb-to-hex-conversion/train/python
DONE
'''


def fromDecToHex(n):
    _hex = ['0', '1', '2', '3', '4', '5', '6'
        , '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    if n > 15:
        data = []
        while n > 0:
            data.append(_hex[n % 16])
            n //= 16
        return "".join(reversed(data))
    else:
        return _hex[n]


def verify(color):
    return max(0, min(color, 255))

def rgb(r, g, b):
    r = verify(r)
    g = verify(g)
    b = verify(b)
    # your code here :)
    hex_r = "0" + fromDecToHex(r) if r < 10 else fromDecToHex(r)
    hex_g = "0" + fromDecToHex(g) if g < 10 else fromDecToHex(g)
    hex_b = "0" + fromDecToHex(b) if b < 10 else fromDecToHex(b)
    return "{0}{1}{2}".format(hex_r, hex_g, hex_b)



print(rgb(0, 0, 0))
print(rgb(127, 127, 127))
print(rgb(1, 1, 1))
print(rgb(255, 255, 255))
print(rgb(148, 0, 211))
print(rgb(255, 255, 300))
print(rgb(-20, 275, 125))
'''
print(fromDecToHex(35361))
print(fromDecToHex(7562))
print(fromDecToHex(255))
'''


if __name__ == '__main__':
    pass
