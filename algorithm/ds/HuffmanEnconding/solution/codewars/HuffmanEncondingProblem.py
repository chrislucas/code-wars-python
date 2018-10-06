'''
https://www.codewars.com/kata/huffman-encoding
https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d/train/python

DONE
'''

from heapq import heappop, heappush


class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.lf = None
        self.ri = None

    def __lt__(self, that):
        return self.frequency < that.frequency

    def __eq__(self, that):
        return self.frequency == that.frequency

    def __str__(self):
        return "Symbol '%s' Freq: %d" % (self.symbol, self.frequency)

    def mapping_code(self, _map, _reverse_mapping, code):
        if self.is_leaf():
            _map[self.symbol] = code
            _reverse_mapping[code] = self.symbol
        else:
            self.lf.mapping_code(_map, _reverse_mapping, code + "0")
            self.ri.mapping_code(_map, _reverse_mapping, code + "1")

    def is_leaf(self):
        return self.lf is None and self.ri is None

    def get_frequency(self):
        return self.frequency if self.is_leaf() else self.lf.frequency + self.ri.frequency

    def get_left(self):
        return self.lf

    def get_right(self):
        return self.ri

    def get_symbol(self):
        return self.symbol


# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    freq = {}
    for i in s:
        freq[i] = freq[i] + 1 if i in freq else 1
    return [(k, v) for k, v in freq.items()]


class Huffman:
    def __init__(self):
        self._map = {}
        self._reverse_mapping = {}

    def renew(self):
        if len(self._map) > 0:
            self._map = {}
        if len(self._reverse_mapping) > 0:
            self._reverse_mapping = {}

    def __str__(self):
        return "%s\n%s" % (self._map, self._reverse_mapping)


huffman = Huffman()


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    if len(freqs) < 2:
        return None

    elif len(s) < 1 or len(freqs) < 1:
        return ""

    heap = []
    for k, v in freqs:
        heappush(heap, Node(k, v))

    while len(heap) > 1:
        p = heappop(heap)
        q = heappop(heap)
        r = Node('+', p.frequency + q.frequency)
        r.lf = p
        r.ri = q
        heappush(heap, r)
    root = heappop(heap)
    huffman.renew()
    root.mapping_code(huffman._map, huffman._reverse_mapping, "")
    _str_encode = ""
    for c in s:
        _str_encode += huffman._map[c]
    print(huffman)
    return _str_encode


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    if len(freqs) < 2:
        return None

    elif len(bits) < 1 or len(freqs) < 1:
        return ""

    _str_decode = ""
    acc = ""
    for i in bits:
        acc += i
        if acc in huffman._reverse_mapping:
            _str_decode += huffman._reverse_mapping[acc]
            acc = ""
    return _str_decode


text = ["aaaabcc"
    , "christoffer"
    , "iiiyiyiiiyyiyyyyiiiiyiyiyiiyyyyyiyyiiiyiyyiyyyyiiiiyiiyyyyiyiyyyyyiyyi"
    , "urgecypmtnahusxvxa"
    , "xfeznsnrdoihkdla"
    , "zlkymwnxzvxcltvrmmkmmuawqxibkchwopgzijllgerpgpssflnperopqdecsaocceovmeotfutooflikymwjrppsn"
        ]
idx = 5
# print(sorted(frequencies(text[0])))
freq = frequencies(text[idx])
str_encode = encode(freq, text[idx])
print(str_encode, len(str_encode))
str_decode = decode(freq, str_encode)
print(str_decode)

if __name__ == '__main__':
    pass
