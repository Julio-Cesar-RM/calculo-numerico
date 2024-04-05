from defs import modulo
a = float(input('Entre com o a: '))
b = float(input('Entre com o valor de b: '))
error = float(input('Entre com o erro: '))
fa = a**3 - 3*(a**2) + 1
fb = b**3 - 3*(b**2) + 1
k = 0
if fa*fb < 0:
    print('Existe uma raiz entre a e b.')
else:
    print('Não existe uma raiz entre a e b, tente novamente.')
while True:
    k = k + 1
    c = (a+b)/2  
    fc = c**3 - 3*(c**2) + 1
    print(f'k = {k} / a = {a} / b = {b} / c = {c} / f(a) = {fa} / f(b) = {fb} / f(c) = {fc} / Erro = {error}')  
    if modulo(fc) < error:
        print(f'c é a raiz aproximada, sendo igual a: {c}.')
        break
    if fa*fc < 0:
        b = c
    else:
        a = c
    fa = a**3 - 3*(a**2) + 1
    fb = b**3 - 3*(b**2) + 1
    input("Pressione Enter para continuar...")

