"""
    Seção 4: Tipo númerico INT

    Corresponde ao conjunto dos inteiros da matemática. Valores numéricos sem casas decimais.
"""

# Tipo int
a = 10
print(a, type(a))
# Neste caso, o tipo é float, embora ainda represente o valor 10.
b = 10.0
print(b, type(b))
print(f'a é igual a b? {a == b}')
print(f'o tipo de a é igual ao de b? {type(a) == type(b)}')

# Operações que retornam inteiros
c = a * a   # retorna int
d = a + 5   # retorna int
e = a - 25  # retorna int
f = a / 1   # retorna float, mesmo que o resultado seja inteiro
g = a // 2  # retorna a parte inteira da divisão, e portanto int
print(f'a * a  = {c}', type(c))
print(f'a + 5  = {d}', type(d))
print(f'a - 25 = {e}', type(e))
print(f'a / 1  = {f}', type(f))
print(f'a // 2 = {g}', type(g))
