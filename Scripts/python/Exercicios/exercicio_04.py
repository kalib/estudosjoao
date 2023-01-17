"""
Vamos aproveitar este exercício para aprender algo novo.
Comentários de muitas linhas. Ao invés de colocar um # no começo de cada linha
de comentário, podemos simplesmente utilizar 3 aspas duplas no começo e novmaente
3 aspas duplas no fim do bloco. E tudo o que existir entre esas 3 aspas duplas
seá considerado pelo Python como um comentário.

Exercício 04:

Crie um programa que calcula a média de notas de um aluno e diga se ele passou de
ano ou não. Parecido com o que fizemos em Bash, porém desta vez em Python:
- O programa deverá perguntar se a pessoa é aluno ou professor:
   - Se for aluno, o programa dará uma mensagem dizendo que apenas professores
   podem executar o sistema e encerra.
   - Se for um professor, o programa segue adiante;
- Pergunta o nome do professor;
- Pergunta o nome do aluno para o qual a média será calculada;
- Recebe 3 variáveis, cada uma delas será uma nota: N1, N2, N3
- Crie uma variável MEDIA que será o resultado da soma das 3 notas dividido por 3.
   - Exemplo: MEDIA = (N1 + N2 + N3) / 3
- Validação da média:
   - Se a média for maior ou igual a 7.0, imprima uma mensagem dizendo que o aluno
   passou de ano.
   - Se a média for menor que 7.0 imprima uma mensagem dizendo que o aluno não passou
   de ano.
"""

resposta = input('você é aluno ou professor? ')

if resposta == 'aluno':
   print('apenas professores podem usar isso')
   exit

if resposta == 'professor':
   print('olá, professor!')
   
   nome_prof = input('professor, qual seu nome? ')
   nome_aluno = input('ok, {}, me diga o nome do aluno em que a média vai ser calculada! '.format(nome_prof))
   
   N1 = float(input('me diga a primeira nota do {} '.format(nome_aluno)))
   N2 = float(input('me diga a segunda nota do aluno {} '.format(nome_aluno)))
   N3 = float(input('me diga a ultima e terceira nota do aluno {} '.format(nome_aluno)))
   
   media = (N1 + N2 +N3) / 3
   
if N1 > 10:
   print('notas maiores que 10 não são permitidas')
   exit

if N2 > 10:
   print('notas maiores que 10 não são permitidas')
   exit

if N3 > 10:
   print('notas maiores que 10 não são permitidas')
   exit

if media > 6:
   print('o aluno {} passou de ano!!! parabens!'.format(nome_aluno))

if media < 6:
   print('o aluno {} infelizmente não passou...'.format(nome_aluno))
   