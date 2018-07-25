'''
https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re
'''


class VigenereCipher(object):

    def __init__(self, key, alphabet):
        _len = len(alphabet)
        self.table = [0] * _len

        for i in range(0, _len):
            self.table[i] = [0] * _len
            self.table[0][i] = alphabet[i]

        for shift in range(1, _len):
            shift %= _len
            for idx in range(0, _len):
                new_idx = (_len - (shift - idx)) if shift > idx else idx - shift
                self.table[shift][new_idx] = alphabet[idx]

    def encode(self, text):
        return ""

    def decode(self, text):
        return ""


abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)


def test(str):
    encode = c.encode(str)
    decode = c.decode(encode)
    print("%s %s %s" % (str, encode, decode))


if __name__ == '__main__':
    pass
