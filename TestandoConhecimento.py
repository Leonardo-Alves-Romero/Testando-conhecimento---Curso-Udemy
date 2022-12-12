nome = input('Qual o seu nome ? ')
idade = input('Qual sua idade ? ')

if nome and idade:
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}.')
    print(f'Seu nome contem {len(nome)} letras.')

    if ' ' in nome:
        print('Seu nome contem espaços.')
    else:
        print('Seu nome não contem espaços')

    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    if int(idade) >= 18:
        print('Você é maior de idade.')
    else:
        print('Você é menor de idade.')
else:
    print('Desculpe, você deixou campos vazios.')