jogador1="X"
jogador2="O"

turn=1
game_on=true

moves=( 1 2 3 4 5 6 7 8 9 )
tempo_inicial=$(date +%s)
welcome_message() {
  echo "==========================================="
  echo "=== Bem vindos ao jogo da velha em bash ==="
  echo "==========================================="
}

get_names () {
  echo "QUal o nome do jogador 1?"
  read jogador1_nome
  echo "Ótimo..."
  echo "Qual o nome do jogador 2?"
  read jogador2_nome
  echo "Ótimo, boa sorte jogadores!"
  echo "============="
}

print_board () {
  clear
  echo " ${moves[0]} | ${moves[1]} | ${moves[2]} "
  echo "-----------"
  echo " ${moves[3]} | ${moves[4]} | ${moves[5]} "
  echo "-----------"
  echo " ${moves[6]} | ${moves[7]} | ${moves[8]} "
  echo "============="
}

player_pick(){
  if [[ $(($turn % 2)) == 0 ]]
  then
    play=$jogador2
    echo -n "$jogador2_nome, ESCOLHA UM QUADRADO: "
  else
    echo -n "$jogador1_nome, ESCOLHA UM QUADRADO: "
    play=$jogador1
  fi

read square
  space=${moves[($square -1)]} 

  if [[ ! $square =~ ^-?[0-9]+$ ]] || [[ ! $space =~ ^[0-9]+$  ]]
  then 
    echo "Quadrado inválido."
    player_pick
  else
    moves[($square -1)]=$play
    ((turn=turn+1))
  fi
  space=${moves[($square-1)]} 
}

check_match() {
  if  [[ ${moves[$1]} == ${moves[$2]} ]]&& \
      [[ ${moves[$2]} == ${moves[$3]} ]]; then
    game_on=false
  fi
  if [ $game_on == false ]; then
    if [ ${moves[$1]} == 'x' ];then
      echo "$jogador1_nome venceu! Parabéns"
      return 
    else
      echo "$jogador2_nome venceu! Parabéns!"
      return 
    fi
  fi
}

check_winner(){
  if [ $game_on == false ]; then return; fi
  check_match 0 1 2
  if [ $game_on == false ]; then return; fi
  check_match 3 4 5
  if [ $game_on == false ]; then return; fi
  check_match 6 7 8
  if [ $game_on == false ]; then return; fi
  check_match 0 4 8
  if [ $game_on == false ]; then return; fi
  check_match 2 4 6
  if [ $game_on == false ]; then return; fi
  check_match 0 3 6
  if [ $game_on == false ]; then return; fi
  check_match 1 4 7
  if [ $game_on == false ]; then return; fi
  check_match 2 5 8
  if [ $game_on == false ]; then return; fi

  if [ $turn -gt 9 ]; then 
    $game_on=false
    echo "Oh oh.. tivemos um empate!"
  fi
}

welcome_message
sleep 2
get_names
sleep 3
print_board
while $game_on
do
  player_pick
  print_board
  check_winner
done
tempo_final=$(date +%s)
tempo_total=$(($tempo_final - $tempo_total))
echo "Esta partida levou ao todo $tempo_total segundos."