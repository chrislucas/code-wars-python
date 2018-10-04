from heapq import heappush, heappop


class MinHeapObj:
    def __init__(self, val):
        self.val = val

    def __lt__(self, that):
        return self.val < that.val

    def __eq__(self, that):
        return self.val == that.val


class MaxHeapObj:
    def __init__(self, val):
        self.val = val

    def __lt__(self, that):
        return self.val < that.val

    def __eq__(self, that):
        return self.val == that.val


class MinHeap:

    def __init__(self):
        self.heap = []

    def heappush(self, val):
        heappush(self.heap, MinHeapObj(val))

    def heappop(self):
        heappop(self.heap)

    def __len__(self):
        return len(self.heap)


if __name__ == '__main__':
    pass
