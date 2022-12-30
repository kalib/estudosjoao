echo "olá, qual seu nome?"
read nome
sleep 1

echo "vocẽ é aluno ou professor?"
read cargo
if [ $cargo != "professor" ]
then
  echo "apenas professores podem usar o script"
  exit
fi 

senha="cuscuz"
echo "qual a senha dos professores?"
read -s senha
if [ $senha == "cuscuz" ]
then 
  echo "correto!"
else
  echo "senha invalida, reinicie o script"
  exit
fi

echo "para qual aluno você deseja calcular a média?"
read aluno
echo "vamos agora calcular a média do $aluno, me diga as notas da primeira, segunda e terceira prova do aluno"
read nota1
read nota2
read nota3

echo "obrigado, agora vou calcular a nota do $aluno, me dé 2 segundos"
sleep 2
media=$(( ($nota1 + $nota2 + $nota3) / 3 ))
sleep 2
echo "a media foi $media"

if [ $media -gt 10 ]
then
  echo "a média não pode ser maior que 10"
elif [ $media -lt 0 ]
then
  echo "medias menores que 0 não podem"
elif [ $media -gt 6 ]
then
  echo "o $aluno passou"
else
  echo "o $aluno reprovou"
fi