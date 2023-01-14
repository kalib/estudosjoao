nome = input('qual seu nome? ')
idade = int(input('qual sua idade? '))
mae = input('qual o nome da sua mãe? ')
mae_idade = int(input('qual a idade da sua mãe? '))

print('\nBem vindo ao sistema, {}. que bom que sua idade é {}.'.format(nome, idade))
print('\nO nome da sua mãe é {}, correto? é um nome bonito. e com {} anos, ela é bem jovem.'.format(mae, mae_idade))

if idade > mae_idade:
    print('deixa de ser mentiroso bixo vei')
    exit()
else:
    print('você tá falando a verdade então')
    esporte = input('qual seu esporte preferido?')
    if esporte == 'natação':
        print('ótimo, tambem adoro natação')
    
#print('você é mais velho que a sua mãe')
#resposta = idade > mae_idade
#print(resposta)
#
#print('vamos ver se sua mãe é mais velha que você')
#print(mae_idade > idade)
#
#print('vocẽ tem certeza que vocẽ não é mais velho que sua mãe? {}'.format(resposta))