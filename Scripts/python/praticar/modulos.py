import time
print('testandkk o o sleep')
time.sleep(1)
print('AAAAAAAAAAAAAAAAAAAAA 2 segundos')
tempo = int(input('quantos segundos você quer que eu espere?'))
print('ok, vou aguardar {} segundos...'.format(tempo))
time.sleep(tempo)
print('ok, eu esperei os {} que você colocou'.format(tempo))