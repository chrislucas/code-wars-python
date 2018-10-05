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


class HuffmanCode:

    def __init__(self):
        self.frequency = {}
        self.root = None
        self._map = {}
        self.str_encode = ""

    def get_encode_str(self):
        return self.str_encode

    def encode(self, _str):
        self._get_frequency(_str)
        self._mapping_encode()
        for s in _str:
            self.str_encode += self._map[s]
        return self

    def _get_frequency(self, _str):
        for i in _str:
            self.frequency[i] = self.frequency[i] + 1 if i in self.frequency else 1
        return

    def _mapping_encode(self):
        p_queue = []
        for k, v in self.frequency.items():
            heappush(p_queue, Node(k, v))
        self.root = self._build_tree(p_queue)
        self.root.mapping_code(self._map, "")

    def decode(self):
        curr = self.root
        dec = ""
        for s in self.str_encode:
            curr = curr.get_left() if s == "0" else curr.get_right()
            if curr.is_leaf():
                dec += curr.get_symbol()
                curr = self.root
        return dec

    def _build_tree(self, p_queue):
        while len(p_queue) > 1:
            p = heappop(p_queue)
            q = heappop(p_queue)
            s = Node('+', p.frequency + q.frequency)
            s.lf = p
            s.ri = q
            heappush(p_queue, s)
        return heappop(p_queue)


text = ["Christoffer Lucas Fernandes sanos", "11112311112311123456"]

compress = HuffmanCode()
encoded = compress.encode(text[0]).get_encode_str()

print(encoded)
print(compress.decode())

if __name__ == '__main__':
    pass
