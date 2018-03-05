'''
https://www.tutorialspoint.com/python/python_reg_expressions.htm
'''

'''
Meta caracteres em regex . ^ $ * + ? { } [ ] \ | ( )

() grupos

$ corresponde ao final da string. Se adicionado a flag multiline \m ira corresponder com 
as string apos o caracter de newline \n
Exemplo $

/r$/ corresponde com a string 'correr' mais nao corresponde com a string 'corre

^ corresponde ao inicio do texto


\b - https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide/Regular_Expressions#special-word-boundary

'''

import re as regex


def test(pattern, _str):
    re_comp = regex.compile(pattern, regex.MULTILINE)
    result = re_comp.match(_str)
    if result is not None:
        print("Result:\nStr: %s\n%s\n%s\n" % (_str, result.span(), result.re))
        re_match = regex.match(pattern, _str)
        if re_match is not None:
            start, end = re_match.start(), re_match.end()
            pos, endpos = re_match.pos, re_match.endpos
            print("Match:\n%s\nStart=%d\nEnd=%d\nsubstr=%s\npe=%s\n"
                  % (re_match, start, end, _str[start:end], _str[pos:endpos]))
    else:
        print("Nao foi encontrado o padrao %s no texto '%s'\n" % (pattern, _str))


'''
Corresponde a um numero que nao comeca com zero
'''
re_num_w_zeros = "^[1-9][0-9]*$"

regex_ip = "[1-9][0-9]*(\.[1-9][0-9]*){1,3}"
regex_ip_2 = "([1-2][0-5]{1,3}|[0-9])(\.([1-2][0-5]{1,3}|[0-9])){1,3}"
regex_ip_3 = "(2[0-5]{2})|(1[0-9]{2})|([1-9][0-9])|([0-9])(\.((2[0-5]{2})|(1[0-9]{2})|([1-9][0-9])|([0-9]))){3}"

test("[a-zA-Z]{1,}", "12321")
test("[a-zA-Z]{1,}", "absc12321")
test("(\d{1,3}){3}", "123.456.789")
test(regex_ip_2, "123.456.789.1")
test(regex_ip_2, "0.0.0.0")

test("[a-z]+r$", "correr")
test("r$", "correr")

if __name__ == '__main__':
    pass
