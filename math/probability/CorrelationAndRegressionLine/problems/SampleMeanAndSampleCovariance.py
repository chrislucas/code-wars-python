'''
https://www.miniwebtool.com/sample-mean-calculator/
https://www.miniwebtool.com/sample-variance-calculator/

https://pt.wikipedia.org/wiki/M%C3%A9dia_e_covari%C3%A2ncia_amostrais

https://ncalculators.com/statistics/covariance-calculator.htm

Covariancia e Correlacao
http://www.mec.ita.br/~denise/teaching/MOQ14/N02_Covariancia_Correlacao.pdf

COVARIÂNCIA E COEFICIENTE DE CORRELAÇÃO
http://www.portalaction.com.br/probabilidades/42-covariancia-e-coeficiente-de-correlacao

'''
import random


def sample_mean(_list):
    return sum(_list) * (1 / len(_list))


def sample_variance(_list, sample_mean):
    acc = 0
    for x in _list:
        acc += (x - sample_mean) * (x - sample_mean)
    return acc / (len(_list) - 1)  # 1/(len(_list)-1)*acc


'''
Se a covariancia for positiva os valores do conjutno X tendem a crescer na mesma
taxa (linear) que os valores do conjunto Y

Se a covariancia for negativa os valores do conjutno X tendem a diminuir na mesma
tax (linear) que os valores de Y

Se a covariancia entre X e T for igual a zero X e Y nao sao correlacionados (
porem segundos um autor nao significa independencia entre as variaveis: 
http://www.portalaction.com.br/probabilidades/42-covariancia-e-coeficiente-de-correlacao).

'Eh possivel medir direção e intensidade da relaçãoestatística entr um par de variávis atraves
da covariancia e o coeficiente de correlacao'

a covariancia indica a direcao das duas variaveis
CV(X, Y)
> 0 positiva
< 0 negativa
= nao ha correlacao

'''

from math import sqrt


def covariance(_list_x, _list_y):
    if len(_list_x) == len(_list_y):
        limit = len(_list_y)
        '''
            A media amostral traca 2 retas num grafico de dispersao, uma vertical
            e uma horizontal, formando 4 quadrantes
            
            Primeiro quadrante
            (x - mx) > 0 e (y - my) > 0 e (x - mx)(y - my) > 0
            Segundo quadrante
            (x - mx) < 0 e (y - my) > 0 e (x - mx)(y - my) < 0
            Terceiro quadrante
            (x - mx) < 0 e (y - my) < 0 e (x - mx)(y - my) < 0
            Quarto quadrante
            (x - mx) > 0 e (y - my) > 0 e (x - mx)(y - my) < 0
            
            Ponto Intenessante: Para uma correlacao positiva, espera-se
            verificar mais pontos no primerio e terceiro quadrando enquanto
            numa correlacao negativa espera-se mais pontos no segundo e quarto quadrante
        '''
        mean_x = sum(_list_x) / len(_list_x)
        mean_y = sum(_list_y) / len(_list_y)
        acc = 0
        for idx in range(0, limit):
            '''
                http://www.mec.ita.br/~denise/teaching/MOQ14/N02_Covariancia_Correlacao.pdf
                x - mean_x -> desvio da media da variavel explicativa,
                y - mean_y -> idem
                (x - mean_x) * (y - mean_y) produto dos desvios
            '''
            acc += (_list_x[idx] - mean_x) * (_list_y[idx] - mean_y)
        return acc / (limit - 1)


# desvio padrao amostral
def sample_standard_deviation(_list, _mean):
    acc = 0
    for xi in _list:
        acc += (xi - _mean) * (xi - _mean)
    return sqrt(acc / (len(_list) - 1))


def correlation_coefficient_v1(_list_x, _list_y):
    limit = len(_list_x)
    _mean_x = sum(_list_y) / limit
    _mean_y = sum(_list_y) / limit
    sx = sample_standard_deviation(_list_x, _mean_x)
    sy = sample_standard_deviation(_list_y, _mean_y)
    acc = 0
    for idx in range(0, limit):
        acc += ((_list_x[idx] - _mean_x) / sx) * ((_list_y[idx] - _mean_y) / sy)
    return acc / (limit - 1)


'''
Ferramenta online para calcular coeficiente de correlacao
http://www.alcula.com/calculators/statistics/correlation-coefficient/
'''


def correlation_coefficient_v2(_list_x, _list_y):
    limit = len(_list_x)
    _mean_x = sum(_list_y) / limit
    _mean_y = sum(_list_y) / limit

    accDiff = 0
    for idx in range(0, limit):
        accDiff += (_list_x[idx] - _mean_x) * (_list_y[idx] - _mean_y)

    accDiffX = 0
    for idx in range(0, limit):
        accDiffX += (_list_x[idx] - _mean_x) * (_list_x[idx] - _mean_x)

    accDiffY = 0
    for idx in range(0, limit):
        accDiffY += (_list_y[idx] - _mean_y) * (_list_y[idx] - _mean_y)

    return accDiff / sqrt(accDiffX * accDiffY)


_list = [x for x in range(1, 10)]
random.shuffle(_list)
print(_list)
sm = sample_mean(_list)
print(sm)
sv = sample_variance(_list, sm)
print(sv)

print(covariance([65.21, 64.75, 65.26, 65.76, 65.96], [67.25, 66.39, 66.12, 65.70, 66.64]))
print(correlation_coefficient_v1([65.21, 64.75, 65.26, 65.76, 65.96], [67.25, 66.39, 66.12, 65.70, 66.64]))
print(correlation_coefficient_v2([65.21, 64.75, 65.26, 65.76, 65.96], [67.25, 66.39, 66.12, 65.70, 66.64]))

if __name__ == '__main__':
    pass
