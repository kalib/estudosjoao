# Faça um programa que leia um número inteiro e mostre na tela
# o seu sucessor e seu antecessor
#
# Por exemplo: se o número que o usuário informar for 5, o programa deverá imprimir:
# O seu número é 5. O antecessor de 5 é 4, o sucessor de 5 é 6.
echo "olá, escolha um numero"
read numero
antecessor=$(($numero - 1))
sucessor=$(($numero + 1))
echo "o antecessor do $numero é igual a $antecessor e o sucessor é igual a $sucessor"