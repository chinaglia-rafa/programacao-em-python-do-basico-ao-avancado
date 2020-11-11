"""
    Seção 4: Strings

    Strings são cadeias de caracteres. Muito mágicas.
"""

a = input("Digite uma palavra para analisarmos: ")
print('Total de caracteres na string:', len(a))
print('A letra "a" aparece na string:', "a" in a)
print('O primeiro caractere na string:', a[0])
print('O último  caractere na string:', a[-1])
print('Todas maiúsculas:', a.upper())
print('Capitalizada:', a.title())
print('Metade da string:', a[:len(a)//2])
