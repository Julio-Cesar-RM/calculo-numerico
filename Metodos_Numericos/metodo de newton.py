from defs import modulo
x0 = float(input('Entre com o X0: '))
error = float(input('Entre com o erro: '))
f = x0**3 - x0 
k = 0
while modulo(f) > error:
    f = x0**3 - x0 
    fl = (3 * (x0**2)) - 1
    if fl == 0:
        print('Erro, a derivada deu zero')
        break
    k += 1
    x = x0 - (f/fl)
    print(f'k = {k} /// x0 = {x0} /// f(x) = {f} /// f(x)der = {fl}')
    x0 = x
    input("Pressione Enter para continuar...")
print(f'A raíz aproximada é: {x0}, e fez com {k} iterações.')
 