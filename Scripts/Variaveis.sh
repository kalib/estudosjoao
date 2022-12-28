echo "seja bem vindo $USER ao script $0"
echo "você me passou os seguintes argumentos: $1, $2"
echo "qual diretorio você deseja verificar?"
read diretorio
echo "ok, aqui está a lista de arquivos do $diretorio"
lista_de_arquivos=$(ls $diretorio)
echo "$lista_de_arquivos"
lista_de_arquivos="nada aqui"
echo "o novo valor de lista de arquivos é $lista_de_arquivos"
echo "esse script levou $SECONDS segundos para executar"