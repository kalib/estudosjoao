numero1 = int(input('me informe um numero inteiro '))
numero2 = int(input('me fale outro numero inteiro '))

if numero1 > numero2:
    print('o numero {} é maior que o numero {}'.format(numero1, numero2))
elif numero1 < numero2:
    print('o numero {} é menor que o numero {}'.format(numero1, numero2))
else:
    print('o numero {} é igual ao numero {}'.format(numero1, numero2))
soma = numero1 + numero2 

print('a soma do numero {} com o numero {} é igual a: {}'.format(numero1, numero2, soma))
if soma > 100:
    print('o seu numero é grande, é mais de 100')
    print('vocẽ se incomoda se eu dividir esse número por 2?')
    resposta = str(input('S ou N '))
    if resposta == 'S':
        divisao = soma / 2
        print('ok, dividindo a soma do numero {} com o numero {} por 2, vai ser igual a: {} '.format(numero1, numero2, divisao))
    elif resposta == 'N':
        print('ok, não vou dividir então')
        exit
    else:
        print('resposta inválida, responda denovo abrindo o progama...')
        exit
else:
    print('o seu número não é maior que 100')