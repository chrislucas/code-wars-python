'''
https://www.codewars.com/kata/huffman-encoding
https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d/train/python
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

    def mapping_code(self, _map, code):
        if self.is_leaf():
            _map[self.symbol] = code
        else:
            self.lf.mapping_code(_map, code + "0")
            self.ri.mapping_code(_map, code + "1")

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
    return freq


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    return ""


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    return ""


if __name__ == '__main__':
    pass