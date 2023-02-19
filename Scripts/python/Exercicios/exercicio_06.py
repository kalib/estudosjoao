'''
Você foi contratado para desenvolver o sistema de uma usina nuclear para controle
de segurança da plataforma de resfriamento.

Uma plataforma de resfriamento será responsável por liberar mais ou menos água quando a temperatura
do reator aumenta ou diminui.

A temperatura ideal do reator deve ser entre 80 e 100 graus celsius.

Se a temperatura ficar abaixo dos 80 graus celsius, todo o fluxo de água deverá ser 0.
Se a temperatura do reator estiver entre 80 e 100 graus celsius, o fluxo de água deve estar no nível 1.
Se a temperatura do reator passar de 100 graus celsius, o fluxo de água deve ser ligado no nível 2.

O seu sistema deverá fazer o seguinte:

Informar que o nível de água no momento é 1.

Em seguida deverá perguntar qual a temperatura atual do reator.
De acordo com a resposta do usuário, ele deverá mudar o nível de água deverá ser ajustado seguindo as regras
de cima.
Após mudar o nível de água, o sistema deverá informar que ajustou o nível de água e que aguardará 30 segundos
para fazer nova verificação.

Após 30 segundos, deverá perguntar ao usuário qual a nova temperatura. Se a nova temperatura ainda estiver
no mesmo nível informado anteriormente (seja menor que 80, maior que 100 ou entre 80-100) e não precisar ajustar
novamente o nível de água, o sistema informará que a temperatura estabilizou e nada mais precisa ser feito agora.

Porém, se a temperatura tiver mudado bastante e o nível de água precisar ser corrigido novamente, o sistema
deverá novamente ajustar o nível de água e informar que aguardará novamente os 30 segundos antes de nova checagem.
'''

import time

print('O nível atual da água é 1')
time.sleep(2)
temp = float(input('Qual a atual temperatura do reator? Em graus Célsius (Cº): '))

if temp < 80:
    print('Temperatura abaixo de 80 Cº, Ajustando o fluxo de água para 0... Aguarde...')

if temp >= 80 and temp <= 100:
    print('Temperatura entre 80 e 100 Cº, Ajustando o fluxo de água para 1... Aguarde...')

elif temp > 100:
    print('Temperatura acima de 100 Cº, Ajustando o fluxo de água para 2... Aguarde...')

time.sleep(5)
print('Fluxo de água ajustado! Atual temperatura: ({} Cº). Aguarde alguns segundos para a nova verificação...'.format(temp))

time.sleep(30)

temp2 = float(input('Qual a atual nova temperatura do reator? Em graus Célsius (Cº): '))
if temp2 < 80:
    print('Temperatura abaixo de 80 Cº, Ajustando o fluxo de água para 0... Aguarde...')

if temp2 >= 80 and temp2 <= 100:
    print('Temperatura entre 80 e 100 Cº, Ajustando o fluxo de água para 1... Aguarde...')

if temp2 > 100:
    print('Temperatura acima de 100 Cº, Ajustando o fluxo de água para 2... Aguarde...')

elif temp2 == temp:
    print('A temperatura está a mesma de antes, Não preciso ajustar.')

time.sleep(2)
print('Obrigado por usar o script! use novamente quando precisar!')
time.sleep(1)

    
    
