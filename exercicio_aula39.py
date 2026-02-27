primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print (f'primeiro valor: "{primeiro_valor}" é maior que segundo valor: "{segundo_valor}"')
elif primeiro_valor < segundo_valor:
    print (f'primeiro valor: "{primeiro_valor}" é menor que segundo valor: "{segundo_valor}"')
elif primeiro_valor == segundo_valor:
    print(f'primeiro valor: "{primeiro_valor}" é igual ao segundo valor: "{segundo_valor}"')

