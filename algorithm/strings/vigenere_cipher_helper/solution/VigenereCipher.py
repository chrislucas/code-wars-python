'''
https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
https://pt.wikipedia.org/wiki/Cifra_de_Vigen%C3%A8re
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
'''


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        _len = len(alphabet)
        self.table = [0] * _len
        self._map = {}
        self.key = key

        for i in range(0, _len):
            self._map[alphabet[i]] = i

        for i in range(0, _len):
            self.table[i] = [0] * _len
            self.table[0][i] = alphabet[i]

        for shift in range(1, _len):
            shift %= _len
            for idx in range(0, _len):
                new_idx = (_len - (shift - idx)) if shift > idx else idx - shift
                self.table[shift][new_idx] = alphabet[idx]

    def __default_process(self, text):
        _len_key = len(self.key)
        encode_text = ""
        idx_key = 0
        for i in range(0, len(text)):
            if text[i] == ' ':
                encode_text += ' '
                continue
            idx_text = self._map[text[i]]
            idx_cypher = self._map[self.key[idx_key]]
            encode_text += self.table[idx_cypher][idx_text]
            idx_key = (idx_key + 1) % _len_key

        return encode_text

    def encode(self, text):
        return self.__default_process(text)

    def __default_decode(self, text):
        _len_key = len(self.key)
        idx_key = 0
        decode_text = ""
        for i in range(0, len(text)):
            if text[i] == ' ':
                decode_text += ' '
                continue
            idx_cypher = self._map[self.key[idx_key]]
            idx_key = 0
            # procurar o indice na linha da tabela
            for x in range(0, self.table[idx_cypher]):
                if self.self.table[idx_cypher][x] == text[i]:
                    idx_key = x
                    break
            decode_text += self._map[idx_key]

        return decode_text

    def decode(self, text):
        return self.__default_decode(text)


def test(alphabet, key, str):
    c = VigenereCipher(key, alphabet)
    encode = c.encode(str)
    decode = c.decode(encode)
    print("%s %s %s" % (str, encode, decode))


test("abcdefghijklmnopqrstuvwxyz", "lemon", "attackatdawn")
test("abcdefghijklmnopqrstuvwxyz", "limao", "atacar base sul")
test("abcdefghijklmnopqrstuvwxyz", "password", "codewars")

if __name__ == '__main__':
    pass
