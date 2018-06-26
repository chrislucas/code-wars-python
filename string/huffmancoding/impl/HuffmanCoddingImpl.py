class Node:
    def __init__(self, _char):
        self.ri = None
        self.lf = None
        self._char = _char
        self.freq = 0

    def __init__(self, lf, ri):
        self.lf = lf
        self.ri = ri
        self._char = '+'
        self.freq = self.ri.freq + self.lf.freq

    def is_leaf(self):
        return self.ri is None and self.lf is None

    def get_left(self):
        return self.lf

    def get_right(self):
        return self.ri

    def acc(self):
        self.freq += 1


class Tree:
    def __init__(self):
        return

    def encode(self, _str):
        self.get_frequency(_str)

    def get_frequency(self, _str):
        frequency = {}
        for c in _str:
            if c in frequency:
                frequency[c] += 1
            else:
                frequency[c] = 1
        return frequency


rootTree = Tree()

rootTree.encode("huffman coding")

print()

if __name__ == '__main__':
    pass
