echo "$USER, qual o seu verdadeiro nome?"
read nome
sleep 1

echo "$nome, qual foi a nota da sua primeira prova?"
read nota1
echo "então sua primeira prova teve a nota $nota1?"
if [ $nota1 -gt 10 ]
then
  echo "notas maiores que 10 são invalidas, reinicie o script"
  exit
fi
sleep 2
echo "qual foi a nota da sua segunda prova?"
read nota2
if [ $nota2 -gt 10 ]
then
  echo "nota maiores que 10 são invalidas, reinicie o script"
  exit
fi
echo "então sua segunda prova teve a nota $nota2?"
sleep 2
echo "por ultimo, qual foi a nota da sua terceira prova?"
read nota3
if [ $nota3 -gt 10 ]
then
  echo "notas maiores que 10 são invalidas, reinicie o script"
  exit
fi

sleep 2
echo "obrigado, um momento enquanto calculo a soma de suas notas..."
sleep 5
soma=$(($nota1 + $nota2 + $nota3))
echo "a soma de suas notas foi: $soma"

sleep 1
echo "ok, agora vamos calcular a média final, me dé um segundo..."
sleep 5
media=$(($soma / 3))
echo "a sua média final é: $media"

sleep 2

echo "vamos ver se você passou de ano ou não..."
sleep 2
if [ $media -gt 6 ]
then
  echo "você..."
  sleep 3
  echo "PASSOU!!"
  sleep 1
  figlet PASSOU!
else
  echo "você..."
  sleep 3
  echo "não passou! tem que estudar mais..."
  sleep 1
  figlet REPROVADO!
fi