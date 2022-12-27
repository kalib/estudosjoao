# Crie um script que execute as seguintes instruções:
#
# 1- Imprima na tela: Bem vindo ao mundo da comida;
# 2- Pergunte ao usuário: "Em primeiro lugar, qual o seu nome?"
# 3- Armazene o nome digitado pelo usuário em uma variável chamada *nome*;
# 4- Imprima na tela: "Seja bem vindo ao mundo da comida, <nome do usuário>!"
# 5- Faça o script esperar 2 segundos
# 6- Pergunte ao usuário: "Qual a sua comida favorita?"
# 7- Salve o valor em uma variável chamada *comida_usuario*;
# 8- Aguarde 2 segundos
# 9- Imprima: "Interessante. Eu não gosto muito de <comida que o usuário digitou>."
# 10- Aguarde 2 segundos
# 11- Imprima: "Qual a sua segunda comida favorita?"
# 12- Armazene a segunda comida em uma variável chamada *comida_usuario_2*;
# 13- Aguarde mais 2 segundos
# 14- Imprima: "Eu acho que a mistura de <nome da comida preferida> com < nome da segunda comida preferida> ficaria estranho"
# 15- Aguarde 1 segundo
# 16- Imprima: "Você é estranho <nome do usuario>, comendo <nomedaprimeira comida preferida> misturado com <nome da segunda comida favorita>"
# 17- Aguarde 2 segundos
# 18- Imprima: "Depois dessa, encerro a nossa conversa. Adeus <nome da pessoa>"
echo "bem vindo ao mundo da comida"
echo "em primeiro lugar, qual o seu nome?"
read nome
echo "seja bem vindo ao mundo da comida, $nome"
sleep 2
echo "qual a sua comida favorita?"
read comida_usuario
sleep 2
echo "interessante. eu não gosto de $comida_usuario"
sleep 2
echo "qual a sua segunda comida favorita?"
read comida_usuario_2
sleep 2
echo "eu acho que a mistura de $comida_usuario com $comida_usuario_2 ficaria estranho"
sleep 1
echo "você é estranho, $nome, comendo $comida_usuario misturado com $comida_usuario_2"
sleep 2
echo "depois dessa, encerro a nossa conversa... adeus $nome"