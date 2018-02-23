# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
# DONE

def duplicate_encode(word):
    #your code here
    mapp = {}
    word = word.lower()
    for c in word:
        if c in mapp.keys():
            mapp[c] += 1
        else:
            mapp[c] = 1
    p = ''.join(['(' if mapp[c] == 1 else ')' for c in word])
    return p


print(duplicate_encode("din"))
print(duplicate_encode("recede"))
print(duplicate_encode("Success"))
print(duplicate_encode("(( @"))

if __name__ == '__main__':
    pass