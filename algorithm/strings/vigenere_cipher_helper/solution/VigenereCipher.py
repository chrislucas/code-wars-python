'''
https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
'''


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        try:
            self.key = key.decode('utf8')
        except:
            self.key = key
        try:
            self.alphabet = alphabet.decode('utf8')
        except:
            self.alphabet = alphabet

        _len = len(self.alphabet)
        self.table = [0] * _len
        self._map = {}

        for i in range(0, _len):
            self._map[self.alphabet[i]] = i

        for i in range(0, _len):
            self.table[i] = [0] * _len
            self.table[0][i] = self.alphabet[i]

        for shift in range(1, _len):
            shift %= _len
            for idx in range(0, _len):
                new_idx = (_len - (shift - idx)) if shift > idx else idx - shift
                self.table[shift][new_idx] = alphabet[idx]

    def __default_encode(self, text):
        try:
            text = text.decode("utf8")
        except:
            pass
        _len_key = len(self.key)
        encode_text = []
        idx_key = 0
        for i in range(0, len(text)):
            if text[i] not in self._map:
                encode_text.append(text[i])
            else:
                idx_text = self._map[text[i]]
                idx_cypher = self._map[self.key[idx_key]]
                encode_text.append(self.table[idx_cypher][idx_text])
            idx_key = (idx_key + 1) % _len_key
        return ''.join(encode_text).encode("utf8")

    def encode(self, text):
        return self.__default_encode(text)

    def __default_decode(self, text):
        try:
            text = text.decode("utf8")
        except:
            pass
        _len_key = len(self.key)
        idx_key = 0
        decode_text = []
        for i in range(0, len(text)):
            if text[i] not in self._map:
                decode_text.append(text[i])
            else:
                idx_cypher = self._map[self.key[idx_key]]
                idx_alpha = -1
                for x in range(0, len(self.table[idx_cypher])):
                    if self.table[idx_cypher][x] == text[i]:
                        idx_alpha = x
                        break
                if idx_alpha > -1:
                    decode_text.append(self.alphabet[idx_alpha])
            idx_key = (idx_key + 1) % _len_key
        return ''.join(decode_text).encode('utf8')

    def decode(self, text):
        return self.__default_decode(text)


def test(text, alpha, key):
    c = VigenereCipher(key, alpha)
    encode = c.encode(text)
    decode = c.decode(encode)
    # c.encode('\xe3\x82\xab\xe3\x82\xbf\xe3\x82\xab\xe3\x83\x8a'), '\xe3\x82\xbf\xe3\x83\xa2\xe3\x82\xbf\xe3\x83\xaf')
    print("Entrada: %s, Encoded: %s, Decoded: %s" % (text, encode, decode))


def test_decode(text, alpha, key):
    c = VigenereCipher(key, alpha)
    return c.decode(text)


def test_encode(text, alpha, key):
    c = VigenereCipher(key, alpha)
    return c.encode(text)


test("codewars", "abcdefghijklmnopqrstuvwxyz", "password")
test("attackatdawn", "abcdefghijklmnopqrstuvwxyz", "lemon")
test("waffles", "abcdefghijklmnopqrstuvwxyz", "password")

test("it's a shift cipher!", "abcdefghijklmnopqrstuvwxyz", "password")
test("\xe3\x82\xab\xe3\x82\xbf\xe3\x82\xab\xe3\x83\x8a", "abcdefghijklmnopqrstuvwxyz", "password")
test("my secret code i want to secure", "abcdefghijklmnopqrstuvwxyz", "password")
test("xt'k o vwixl qzswej!", "abcdefghijklmnopqrstuvwxyz", "password")
test("it's w ziruw qhaaqs!", "abcdefghijklmnopqrstuvwxyz", "password")

# test_decode("xt'k s ovzii cahdsi!", "abcdefghijklmnopqrstuvwxyz", "password")
# test_encode("it's a shift cipher!", "abcdefghijklmnopqrstuvwxyz", "password")
# test_decode("xt'k o vwixl qzswej!", "abcdefghijklmnopqrstuvwxyz", "password")


test("CODEWARS", "abcdefghijklmnopqrstuvwxyz", "password")
test("atacar base sul", "abcdefghijklmnopqrstuvwxyz", "limao")

'''

'''

if __name__ == '__main__':
    pass
