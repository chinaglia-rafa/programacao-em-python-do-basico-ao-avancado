"""
    Seção 3: entrada de dados com input()

    O comando input recebe uma entrada de dados do usuário e a retorna como string.
"""

# Entrada simples

ipt = input("Entre com algum dado: ")
print(type(ipt))

# A questão da tipagem

# Errado
# idade = input("Digite sua idade: ")
# print(f'Você tem {100 - idade} anos para chegar aos 100 anos idade!')

# Certo
idade = int(input("Digite sua idade: "))
print(f'Você tem {100 - idade} anos para chegar aos 100 anos idade!')

# Garantir que a conversão pode ser feita na entrada
try:
    idade = int(input("Digite a sua idade (nada de letras hein!!): "))
    print(f'{idade} foi convertido com sucesso para int!')
except ValueError:
    print('Valor digitado não pode ser convertido para int!')
