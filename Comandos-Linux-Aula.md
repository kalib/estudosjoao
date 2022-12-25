# Estudos Linux
###GERENCIAMENTO DO SISTEMA 

- **pwd**- sabe onde está
- **cd**- mudar diretorio
- **ls**- ver diretorios e arquivos
- **..-** um nivel de diretorio
- **/** - pular de diretorios 
- **cd (sem nada)** - volta para o ponto de origem
- **ls  -lh** - mostra o tamanho do arquivo na forma humana
- **ls  -lha** - mostra arquivos ocultos de um diretorio
- **cd ~/exemplo** - leva pro diretorio que voce colocou depois do /
- **tree** - mostra a arvore de diretorios e arquivos
- **clear** - limpar os textos no terminal
- **uptime** - mostra a quanto tempo o sistema está ligado
- **mkdir** - criar um diretorio
- **mkdir -p** - criar um caminho completo
- **touch** - criar um arquivo
- **&&** - pode ser utilizado entre dois comandos, para executar dois comandos
    - exemplo: 
    ```
    mkdir pasta1 && cd pasta1/ && touch arquivo1
    ```
- **cp** - copia um arquivo para um diretorio (tem que colocar primeiro o arquivo e depois o destino)
- **mv** - move um arquivo para um diretorio, mas tambem pode ser usado para renomear (primeiro o arquivo e depois o destino)

###GERENCIAMENTO DE PACOTES

- **sudo apt update** - atualizar os progamas e repositorios desatualizados
- **sudo apt search** - procurar um progama
- **sudo apt install** - instalar um progama

###INFORMAÇÕES DO SISTEMA

- **uname -a** - lista informações do sistema 

###GERENCIAMENTO DE USUARIOS

- **who** - mostrar todos os usuarios logados no momento
- **whoami** - mostrar o usuario que digitou o comando 
- **sudo adduser (nome)** - criar um usuario
- **su (nome de usuario)** - logar com outro usuario
- **sudo passwd (nome de usuario)** - editar a senha do usuario
- **logout** - deslogar do usuario atual
- **userdel -r** - deletar um usuario e tudo dele

###MANIPULAÇÃO DE ARQUIVOS

- **unzip** - extrair
- **cat** - mostra o conteudo de um arquivo
- **more** - abre o arquivo somente para leitura, pode apertar Q para fechar
- **vim** - editar arquivos
- **rm** - deletar arquivos
- **rm -r** - deletar um diretorio com coisas dentro
- **rmdir** - deletar um diretorio com nada dentro

###VIM

- para abrir o modo editar, aperte I
- para voltar o modo de comandos, pressione ESC
- **:** - inicia comandos
- para salvar o arquivo pressione " w" no modo de comando depois do :
- para deletar uma linha inteira, aperte a tecla "d" duas vezes no modo de comando
- para fechar e salvar um arquivo, precisa estar no modo de comando e escrever ":wq" sem as aspas
- para fechar um arquivo de forma forçada sem salvar, entre no modo de comando e digite ":q!" sem as aspas
- para copiar uma linha inteira, vá ate a linha e aperte a tecla "y" duas vezes, tem que estar no modo de comando, e para colar aperte "p"
- para copiar uma certa quantidade de linhas, vá até a linha que vai ser a primeira linha para copiar, aperte "y" na linha e depois escreva o quanto de linhas que você quer copiar, depois aperte "y" denovo, e para colar aperte "p", precisa estar no modo de comando. por exemplo: para copiar 10 linhas, aperte "y10y" sem as aspas
- e para desfazer a ultima edição/operação, aperte a tecla "u" sem aspas apenas uma vez no modo de comando

###VSCODE

- **shift+crtl+↑/↓** seleciona multiplas linhas (apenas o começo)
- **shift+crtl+alt+↑/↓** duplica uma linha
- **+crtl+alt+←/→** vai para o final da próxima palavra