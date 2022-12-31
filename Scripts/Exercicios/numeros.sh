# Escreva um programa que realize as seguintes tarefas:
# - Pergunte o nome do usuário e em seguida dê uma mensagem de boas vindas para o usuário.
# - Informe ao usuário que este programa calcula o IMC - Índice de Massa Corporal.
# - Informe que o cálculo do IMC ajuda a identificar se a pessoa está acima do seu peso ideal ou abaixo.
# -  Comece perguntando a altura da pessoa em centímetros, ou seja, se a pessoa tem 1,40 de altura, a altura dela é 140.
# - Em seguida pergunte o peso dessa pessoa.
# - Informe que voce irá calcular o IMC da pessoa.
# - A fórmula do IMC é: Peso / ( altura * altura)
# - Ao calcular o IMC, informe o resultado do IMC para a pessoa.
# - Para calcular se a pessoa está acima ou abaixo do peso ideal utilize as seguintes informações:
### - Se o IMC der menor que 18, informe que a pessoa está com magreza, abaixo do peso ideal..
### - Se o IMC der entre 18 e 25, informe que a pessoa está com o peso ideal..
### - Se o IMC der entre 25 e 30, informe que a pessoa está acima do peso ideal..
### - Se der acima de 31, informe que a pessoa está com algum grau de obesidade.
# - Informe o resultado final ao usuário
echo "olá, qual seu nome?"
read nome
echo "olá, $nome"
echo "este progama serve para calcular o IMC, e tambem o IMC ajuda a identificar se a pessoa está acima do peso ou não"
echo "mas enfim, me diga sua altura em centimetros"
read altura
echo "por ultimo, me diga o seu peso"
read peso
echo "irei calcular o seu IMC"
IMC=$(($peso / ($altura * $altura) ))
echo "o seu IMC é $IMC"
if [$IMC lt 18]
then
  echo "você está com magreza, você está abaixo do peso ideal"
  exit
elif [$IMC ge 18 25]
then
  echo "você está com o peso ideal"
  exit
elif [$IMC ge 25 30]
then
  echo "vocẽ está acima do peso ideal"
  exit
elif [$IMC gt 31]
then
  echo "vocẽ está com algum grau de obesidade"
  exit
fi