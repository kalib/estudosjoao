#!/bin/bash
# este é o meu primeiro script
nome_arquivo="TesteShell.txt"
nome_diretorio="/home/tux/diretorio-do-shell"
nome_arquivo2="TesteShell2.txt"
cowsay iniciando o script
sleep 3
clear
echo "Olá Mundo!"
echo "Bem vindo ao meu primeiro script em shell."
echo ""
sleep 3
clear
echo "Criando diretorio de teste"
rm -r $nome_diretorio
mkdir $nome_diretorio
echo ""
sleep 3
echo "criando o arquivo"
touch $nome_diretorio/$nome_arquivo
echo ""
sleep 3
clear
ls $nome_diretorio/$nome_arquivo
clear
echo ""
sleep 3
echo "testando comando em shell" > $nome_diretorio/$nome_arquivo
echo "renomeando o arquivo"
mv $nome_diretorio/$nome_arquivo $nome_diretorio/$nome_arquivo2
ls $nome_diretorio/$nome_arquivo2
cat $nome_diretorio/$nome_arquivo2