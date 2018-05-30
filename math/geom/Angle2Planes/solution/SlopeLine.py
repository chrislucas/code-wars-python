'''
http://www.codewars.com/kata/slope-of-a-line
DONE
'''


def getSlope(p1, p2):
    '''
    Return the slope of the line through p1 and p2
    '''
    if p2[0] - p1[0] == 0:
        return None
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


print(getSlope([1, 1], [2, 2]))
print(getSlope([11, 1], [1, 11]))
print(getSlope([1,1],[1,2]))
print(getSlope([1,1],[1,1]))

if __name__ == '__main__':
    pass
