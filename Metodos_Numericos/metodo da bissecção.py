from defs import modulo
a = float(input('Entre com o a: '))
b = float(input('Entre com o valor de b: '))
error = float(input('Entre com o erro: '))
fa = a**2 + a - 6
fb = b**2 + b - 6
k = 0
if fa*fb < 0:
    print('Existe uma raiz entre a e b.')
else:
    print('Não existe uma raiz entre a e b, tente novamente.')
while True:
    k = k + 1
    print(f'k = {k} /// a = {a} /// b = {b} /// f(a) = {fa} /// f(b) = {fb} /// Erro = {error}')
    c = (a+b)/2
    fc = c**2 + c - 6
    if modulo(fc) < error:
        print(f'c é a raiz aproximada, sendo igual a: {c}.')
        break
    if fa*fc < 0:
        b = c
    else:
        a = c
    fa = a**2 + a - 6
    fb = b**2 + b - 6
    input("Pressione Enter para continuar...")

