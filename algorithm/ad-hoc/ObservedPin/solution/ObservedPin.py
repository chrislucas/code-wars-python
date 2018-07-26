'''
https://www.codewars.com/kata/the-observed-pin/train/python
'''


def build_matrix_neighbor():
    neighbors = [[]] * 10
    neighbors[0] = [8]
    neighbors[1] = [2, 4]
    neighbors[2] = [1, 3, 5]
    neighbors[3] = [2, 6]
    neighbors[4] = [1, 5, 7]
    neighbors[5] = [2, 4, 6, 8]
    neighbors[6] = [3, 5, 9]
    neighbors[7] = [4, 8]
    neighbors[8] = [0, 5, 7, 9]
    neighbors[9] = [6, 8]
    return neighbors


def get_pins(observed):
    neighbors = build_matrix_neighbor()
    digits = observed[0]
    _len_digits = len(digits)
    ans = []
    for i in digits:
        digits_neighbors = neighbors[int(i)]
        ans.append(digits_neighbors)

    return ans


expectations = [('8', ['5', '7', '8', '9', '0'])
    , ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"])
    , ('369', ["339", "366", "399", "658", "636", "258", "268", "669"
        , "668", "266", "369", "398", "256", "296", "259", "368", "638", "396"
        , "238", "356", "659", "639", "666", "359", "336", "299", "338", "696"
        , "269", "358", "656", "698", "699", "298", "236", "239"]
       )
                ]

for tup in expectations:
    sorted(get_pins(tup[0]))
    sorted(tup[1])

if __name__ == '__main__':
    pass
