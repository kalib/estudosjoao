# Escreva um script que pergunte ao usuário dois números (numero1 e em seguida numero2)
# Em seguida o programa irá comparar estes números:
# Se o numero1 for maior que o numero 2, imprima: O seu numero1 é maior que o seu numero2.
# Se o numero 2 for maior que o numero1, imprima: o seu numero2 é maior que o seu numero1.
echo "oi, qual o seu nome?"
read nome
sleep 1
echo "olá $nome"
sleep 1
echo "$nome, me diga dois numeros, por favor"
read numero1
read numero2
if [ $numero2=$numero1 ]
then
  figlet ERRO ENCONTRADO!!!
  sleep 3
  echo "não pode repetir numeros pois isso quebra o script, reinicie o script e não coloque os mesmos numeros nas duas perguntas"
  sleep 2
  echo "fechando o script em 3 segundos..."
  sleep 3
  exit
fi
sleep 1
echo "obrigado, agora vou analisar se o numero $numero1 é maior que o numero $numero2, ou vice versa"
if [ $numero1 -gt $numero2 ]
then
  sleep 2
  echo "o numero $numero1 é maior que o numero $numero2"
else
  sleep 2
  echo "o numero $numero2 é maior que o numero $numero1"
fi