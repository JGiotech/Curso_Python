
nome = (input('Digite o seu nome:'))
idade =(input('Digite sua idade:'))

if nome and idade:
    print(f'seu nome é: {nome}')
    print(f'sua idade é: {idade}')
    print(f'seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('seu nome contem espaços')
    else:
        print('seu nome nao contem espaços')

    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpa, voce deixou campos vazios')

    





