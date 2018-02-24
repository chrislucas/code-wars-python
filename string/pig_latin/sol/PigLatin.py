# https://www.codewars.com/trainer/python


def pig_it(text):
    return " ".join([sub[1:len(sub)] + sub[0] + "ay" if sub.isalpha() else sub for sub in text.split(" ")])


print(pig_it("Pig latin is cool"))
print(pig_it("This is my string"))
print(pig_it("Hello world !"))


if __name__ == '__main__':
    pass