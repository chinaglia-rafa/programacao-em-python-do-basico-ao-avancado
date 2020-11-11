"""
    Seção 4: O tipo booleano

    O tipo booleano representa valores binários, 1 ou 0, na forma True ou False.
"""

a = 10 > 5
print(f'10 é maior que 5? {a}', type(a))

# Booleanos podem ser resultados de expressões complexas
b = 10 > 3 or (a and False) and 5 == 5
print(f'b = {b}', type(b))
