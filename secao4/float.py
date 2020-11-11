"""
    Seção 4: Tipo numérico Float

    Representa valores com casas decimais.
"""

import math

try:
    a = float(input("Digite um valor com casas decimais (ex.: 5.2):"))
    print(f'Valor digitado: {a}', type(a))
except ValueError:
    print("Ops! Valor não pôde ser convertido.")

# Valores do tipo float sempre retornam valores do tipo float em operações
b = 10.0 + 5.0
c = 10.0 + 5
d = 2.0 * 2.5
e = 10.0 // 2
f = 10.0 % 2
print(f'{b}', type(b))
print(f'{c}', type(c))
print(f'{d}', type(d))
print(f'{e}', type(e))
print(f'{f}', type(f))

# O tipo float pode variar de precisão se necessário
print(f'math.pi = {repr(math.pi)}')
print(f'math.pi = {format(math.pi, ".2f")}')    # C style
print(f'math.pi = {format(math.pi, ".12g")}')
print(f'math.pi = {format(math.pi, ".40g")}')
