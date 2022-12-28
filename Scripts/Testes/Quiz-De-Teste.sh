echo "Olá! bem vindo ao quiz de hoje!"
sleep 1
echo "Vamos começar o quiz! Mas... preciso de uma pequena informação sua..."
sleep 1
echo "E não, Essa informação é nada muito pessoal como a senha de algo seu ou algo assim, é apenas o seu nome!"
read nome
sleep 1
echo "Ok telespectadores, Hoje quem vai participar do quem quer ser milionario é... $nome!"
sleep 1
echo "."
sleep 1
echo "ok, então para começar e terminar até porque vai ser apenas uma pergunta, irei fazer uma pergunta simples"
sleep 1
echo "."
echo "qual a forma da água que você consegue armazenar em algum recipiente sem problemas?"
sleep 1
echo "Respostas: A: Sólida, B: Liquida, C: Nenhuma das alternativas anteriores"
echo "."
echo "(alerta na hora de responder, escreva a letra da resposta no modo maiusculo, se não o script não funciona)"
read B
if [ $B=B ]
then
  sleep 1
  echo "você acertou!!!"
else
  echo "Que pena, na próxima você acerta!"
fi