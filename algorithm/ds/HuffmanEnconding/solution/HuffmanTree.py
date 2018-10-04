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


def _get_frequency(_str):
    freq = {}
    for i in _str:
        freq[i] = freq[i] + 1 if i in freq else 1
    return freq


def mapping_encode(_str, _map):
    frequency = _get_frequency(_str)
    pqueue = []
    for k, v in frequency.items():
        heappush(pqueue, Node(k, v))
    _root_node = _build_tree(pqueue)
    _root_node.mapping_code(_map, "")
    return _root_node


def encode(_str, _map):
    code = ""
    for s in _str:
        code += _map[s]
    return code


def decode(_str, root):
    curr = root
    dec = ""
    for s in _str:
        curr = curr.get_left() if s == "0" else curr.get_right()
        if curr.is_leaf():
            dec += curr.get_symbol()
            curr = root
    return dec


def _build_tree(pqueue):
    while len(pqueue) > 1:
        p = heappop(pqueue)
        q = heappop(pqueue)
        s = Node('+', p.frequency + q.frequency)
        s.lf = p
        s.ri = q
        heappush(pqueue, s)
    return heappop(pqueue)


_map = {}
_root = mapping_encode("11112311112311123456", _map)

_str_encode = encode("11112311112311123456", _map)
print(_str_encode)

_str_decode = decode(_str_encode, _root)
print(_str_decode)

if __name__ == '__main__':
    pass
