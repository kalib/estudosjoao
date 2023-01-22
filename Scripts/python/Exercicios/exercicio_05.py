"""
Utilizando o código do exercício anterior, vamos melhorar a usabilidade do sistema de média de notas:

Exercício 05:
Crie um programa que calcula a média de notas de um aluno e diga se ele passou de
ano ou não. 

Muito parecido com o que fizemos no exercício anterior, porém com a utilização de funções.

O programa deverá ter 3 funções:
    - checa_professor()
    - calcula_media_aluno()
    - da_resultado_de_aprovacao()

A função checa_professor deverá perguntar se a pessoa é um aluno ou professor:
   - Se for aluno, o programa dará uma mensagem dizendo que apenas professores
   podem executar o sistema e encerra.
   - Se for um professor, o programa segue adiante;
   - Pergunta o nome do professor;
   - Em seguida chama a função calcula_media_aluno;

A função calcula_media_aluno deverá fazer o seguinte:
    - Pergunta o nome do aluno para o qual a média será calculada;
    - Recebe 3 variáveis, cada uma delas será uma nota: N1, N2, N3
        - Se alguma das notas for menor que 0.0 ou maior que 10.0, uma mensagem deverá ser passada dizendo que a nota é inválida
        e o sistema deverá iniciar a função calcula_media_aluno novamente;
    - Crie uma variável MEDIA que será o resultado da soma das 3 notas dividido por 3.
    - Exemplo: MEDIA = (N1 + N2 + N3) / 3
    - Em seguida o sistema deverá chamar a função da_resultado_de_aprovacao;

A função da_resultado_de_aprovacao deverá fazer o seguinte:    
    - Validação da média:
        - Se a média for maior ou igual a 7.0, imprima uma mensagem dizendo que o aluno
        passou de ano.
        - Se a média for menor que 7.0 imprima uma mensagem dizendo que o aluno não passou
        de ano.
"""


def checa_professor():
    pergunta = input('vocẽ é um professor ou um aluno? ')
    if pergunta == 'aluno':
        print('alunos não podem usar este script')
        exit
    
    if pergunta == 'professor':
        nome_P = input('olá professor, qual seu nome? ')
        print('bom te conhecer, {}'.format(nome_P))
        calcula_media_aluno()

def calcula_media_aluno():
    nome_A = input('professor, qual o nome do aluno em que vocẽ deseja calcular a média?')
    print('agora me diga as notas do aluno {}, a primeira, a segunda, e a terceira nota'.format(nome_A))
    
    N1 = float(input('nota 1 = '))
    N2 = float(input('nota 2 = '))
    N3 = float(input('nota 3 = '))
    
    if N1 > 10.0:
        print('você não pode usar notas maiores que 10')
        calcula_media_aluno()
    
    if N1 < 0.0:
        print('notas menores que 0 não são permitidas')
        calcula_media_aluno()
    
    if N2 > 10.0:
        print('notas maiores que 10 não são permitidas')
        calcula_media_aluno()
        
    if N2 < 0.0:
        print('notas menores que 0 não são permitidas')
        calcula_media_aluno()
        
    if N3 > 10.0:
        print('notas maiores que 10 não são permitidas')
        calcula_media_aluno()
        
    if N3 < 0.0:
        print('notas menores que 0 não são permitidas')
        calcula_media_aluno()
        
    media = (N1 + N2 + N3) / 3
    
    da_resultado_de_aprovacao()

def da_resultado_de_aprovacao():
    if media > 6.9:
        print('o aluno {} passou de ano'.format(nome_A))
        exit
    if media < 6.9:
        print('o aluno {} não passou de ano'.format(nome_A))

checa_professor()