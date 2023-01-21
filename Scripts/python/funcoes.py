def dar_boas_vindas():
    print('olá, seja bem vindo {}'.format(nome))
    
def calcular_idades():
    print('vou calcular a diferença da idade de sua mãe e da sua idade')
    diferenca = idade_mae - idade
    print(' a diferença da idade da sua mãe e a sua idade é {}'.format(diferenca))
    
   

def escolher_esporte():
    pergunta_esporte = input('vocẽ gosta de esportes? sim ou nao? ')
    if pergunta_esporte == 'sim':
        
        esporte = input('qual seu esporte favorito? ')
        print('eu tambem gosto de {}'.format(esporte))
        
        sugerir_esporte(esporte)
        
    elif pergunta_esporte == 'nao':
        print('que pena que você não gosta de esportes, adeus!')
        exit()
    else:
        print('resposta inválida, tente novamente')
        escolher_esporte()
        
def sugerir_esporte(esporte):
    print('já que você gosta do esporte {}, eu sugiro que você tambem tente praticar futebol'.format(esporte))

nome = input('qual seu nome? ')
idade = int(input('qual sua idade? '))
idade_mae = int(input('qual a idade da sua mãe? '))

esporte = ''

dar_boas_vindas()
calcular_idades()

escolher_esporte()

print('as variaveis que vocẽ usou foram: nome, idade, e idade_mae')
print('valor da variavel nome: {}'.format(nome))
print('valor da variavel idade: {}'.format(idade))
print('valor da variavel idade_mae: {}'.format(idade_mae))
