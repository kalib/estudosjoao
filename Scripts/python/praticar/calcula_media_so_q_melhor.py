def professor_ou_aluno():
    nome_prof = input('Olá, pessoa que está utilizando este progama, qual seu nome? ')
    resposta = input('olá, {} Você é um professor, diretor ou aluno? '.format(nome_prof))
    
    if resposta == 'aluno':
        print('Alunos não podem usar este progama, apenas professores, o diretor ou pessoas com permissão')
        exit

    if resposta == 'professor':
        print('olá professor {}, seja bem vindo!'.format(nome_prof))
        aluno()

    elif resposta == 'diretor':
        print('olá diretor {}, seja bem vindo!'.format(nome_prof))
        aluno()

def aluno():
    nome_aluno = input('{} {}, qual o nome do aluno em que você deseja calcular a média e ver as notas? '.format(resposta, nome_prof))
    
    if nome_aluno == nome_prof:
        print('uh, o {} tem o mesmo nome do aluno? suspeito... mas enfim, vamos ver as notas do aluno do aluno {}'.format(resposta, nome_aluno))
        nota()
    else:
        print ('ok, {} {}, agora vamos ver as notas do aluno {}'.format(resposta, nome_prof, nome_aluno))
        nota()

def nota():
    N1 = float(input('me diga a primeira nota do aluno: '))
    N2 = float(input('me diga a segunda nota do aluno: '))
    N3 = float(input('me diga a terceira nota do aluno: '))
    N4 = float(input('me diga a quarta nota do aluno: '))
    N5 = float(input('me diga a quinta e ultima nota do aluno: '))
    
    if N1 > 10.0:
        print('ERRO! NOTA MAIOR QUE 10.0, TENTE DENOVO!')
        nota()
    if N1 < 0.0:
        print('ERRO! NOTA MENOR QUE 0.0, TENTE DENOVO!')
        nota()
    if N2 > 10.0:
        print('ERRO! NOTA MAIOR QUE 10.0, TENTE DENOVO!')
        nota()
    if N2 < 0.0:
        print('ERRO! NOTA MENOR QUE 0.0, TENTE DENOVO!')
        nota()
    if N3 > 10.0:
        print('ERRO! NOTA MAIOR QUE 10.0, TENTE DENOVO!')
        nota()
    if N3 < 0.0:
        print('ERRO! NOTA MENOR QUE 0.0, TENTE DENOVO!')
        nota()
    if N4 > 10.0:
        print('ERRO! NOTA MAIOR QUE 10.0, TENTE DENOVO!')
        nota()
    if N4 < 0.0:
        print('ERRO! NOTA MENOR QUE 0.0, TENTE DENOVO!')
        nota()
    if N5 > 10.0:
        print('ERRO! NOTA MAIOR QUE 10.0, TENTE DENOVO!')
        nota()
    if N5 < 0.0:
        print('ERRO! NOTA MENOR QUE 0.0, TENTE DENOVO!')
        nota()
    
    resposta2 = input('{} {}, você tem certeza de que as notas estão corretas? eu irei repetir as notas: Nota1 = {}, Nota2 = {}, Nota3 = {}, Nota4 = {}, Nota5 = {}. Está tudo certo? escreva "sim" ou "não": '.format(resposta, nome_prof, N1, N2, N3, N4, N5))
    if resposta2 == 'sim':
        print('ok, vamos calcular a média do aluno {} '.format(nome_aluno))
        media_nota()
    if resposta2 == 'não':
        print('Ok, resetando a função "nota" para reescrever a nota...')
        nota()
    else:
        print('eu não entendi sua resposta, reiniciando a função "nota" do zero... (respostas disponiveis: "sim" ou "não" só que sem as aspas!)')
        nota()

def media_nota():
    print('ok, {} {}, vamos calcular a média do aluno {}!'.format(resposta, nome_prof, nome_aluno))
    media = (N1 + N2 + N3 + N4 + N5 ) / 5
    print('média criada, agora vamos ver se o aluno passou...')

def resultado():
    if media > 6.9:
        print('Boa! o aluno passou!!')
        exit
    if media < 6.9:
        print('infelizmente o aluno não passou')

media = ''
N1 = ''
N2 = ''
N3 = ''
N4 = ''
N5 = ''
resposta = ''
nome_prof = ''
nome_aluno = ''
professor_ou_aluno()