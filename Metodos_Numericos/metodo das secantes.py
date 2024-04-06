from defs import modulo
x0 = float(input('Entre com o valor de x0: '))
x1 = float(input('Entre com o valor de x1: '))
error = float(input('Entre com o erro: '))
fx0 = x0**3 - 3*(x0**2) + 1
fx1 = x1**3 - 3*(x1**2) + 1
k = 1
x2 = ((x0*fx1)-(x1*fx0)) / (fx1-fx0)
while True:
    print(f'x0 = {x0} / x1 = {x1} / fx0 = {fx0} / fx1 = {fx1} / k = {k} / x2 = {x2} / erro = {error}')
    x0 = x1
    x1 = x2
    fx0 = x0**3 - 3*(x0**2) + 1
    fx1 = x1**3 - 3*(x1**2) + 1
    k = k + 1
    if fx1-fx0 == 0:
        print(f'O limite do programa foi atingido. A raiz aproximada achada foi de x2: {x2}.')
        break
    x2 = ((x0*fx1)-(x1*fx0))/(fx1-fx0)
    input("Pressione Enter para continuar...")
    if modulo(x2) < error:
        print('x2 é a raiz aproximada, sendo igual a:')
        print(x2)
        break
