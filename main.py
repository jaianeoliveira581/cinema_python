nome = input('informe seu nome: ')
idade = input('informe sua idade: ')
sala = int(input('Informe o número da sala de 1 a 5: '))

while True:
    nome = input('informe nome do filme: ')
    if nome != '':
    idade = int(imput('informe sua idade: '))
    if idade >= 18:
        print(f'{filme} é maior de idade. ')
    else:
        print(f'(filme)é menor de idade: ')

print('lista de filmes\n')
print('sala 1 - Filme A Volta dos Que Não Foram. ')
print('sala 2 - Filme A Roda Quadrada. ')
print('sala 3 - Filme Poeira em Alto Mar. ')
print('sala 4 - Filme As Tranças do Rei Careca. ')
print('sala 5 - Filme A Vingança do Peixe Frito. ')

if sala < 18:
    print(f'classificação indicativa 10')
elif sala >= 10:
    print(f'clasificação indicativa 12')
elif sala >= 12:
    print(f'classificação indicativa 16')
elif sala >= 16:
    print(f'classificação indicativa 18')
elif sala >= 18:
    print(f'livre')
else: 
    print(f'sala inexistente')

sala = int(input('informe a sala desejada: '))

match sala:
    case 1:
        print(f'Filme escolhido por (nome) A Volta dos Que Não Foram.')
    case 2:
        print(f'filme escolhido por (nome) A Roda Quadrada.')
    case 3:
        print(f'filme escolhido por (nome) Poeira em Alto Mar.')
    case 4:
        print(f'filme escolhido por (nome) As Tranças do Rei Careca.')
    case 5:
        print(f'filme escolhido por (nome) A Vingança do Peixe Frito.')
    case _:
        print('Sala inexistente.')