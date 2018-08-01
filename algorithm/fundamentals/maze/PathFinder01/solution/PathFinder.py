'''
https://www.codewars.com/kata/path-finder-number-1-can-you-reach-the-exit/train/java
DONE
'''


def test(x1, y1, x2, y2):
    return x1 == x2 and y1 == y2


def path_finder(maze):
    matrix = [list(i) for i in maze.split("\n")]
    w = len(matrix[0])
    h = len(matrix)
    memo = [[False] * w for i in range(h)]
    # direita, esquerda, cima, baixo,
    possible_steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    if matrix[w - 1][h - 1] == 'W':
        return False

    possible_path = [(0, 0)]
    while len(possible_path) > 0:
        current_local = possible_path[0]
        possible_path.pop(0)
        if test(current_local[0], current_local[1], w - 1, h - 1):
            return True
        memo[current_local[0]][current_local[1]] = True
        for p in possible_steps:
            x = current_local[0] + p[0]
            y = current_local[1] + p[1]
            if 0 <= x < w and 0 <= y < h and not memo[x][y] and matrix[x][y] == '.':
                possible_path = [(x, y)] + possible_path

    return False


a = "\n".join([
    ".W.",
    ".W.",
    "..."
])

b = "\n".join([
    ".W.",
    ".W.",
    "W.."
])

c = "\n".join([
    "......",
    "......",
    "......",
    "......",
    "......",
    "......"
])

d = "\n".join([
    "......",
    "......",
    "......",
    "......",
    ".....W",
    "....W."
])

print(path_finder(a))
print(path_finder(b))
print(path_finder(c))
print(path_finder(d))

if __name__ == '__main__':
    pass
