import time


def Nome_apresentacao():

    print('Olá, usuário')
    
    time.sleep(1.3)
    nome = input('Qual seu nome?')
    time.sleep(1)
    
    print('Seja bem vindo, {}, espero que vocẽ goste do script!, Você terá que responder umas perguntas meio pessoais, espero que não se incomode!'.format(nome))
    time.sleep(3.5)
    Idade_apresentacao(nome)

def Idade_apresentacao(nome):
    
    idade = input('{}, Qual sua idade?'.format(nome))
    time.sleep(1.7)
    
    print('Então sua idade é {}?, legal!'.format(idade))
    time.sleep(3.5)
    Nasc_apresentacao(nome,idade)

def Nasc_apresentacao(nome,idade):
    
    nasci = input('{}, Em que data você nasceu?'.format(nome))
    time.sleep(1.7)
    
    print('{}, Legal, vocẽ nasceu no dia {}'.format(nome,nasci))
    time.sleep(3.5)
    comfav(idade,nome,nasci)

def comfav(idade,nome,nasci):
    
    comfav = input('{}, bom, já fiz algumas perguntas pessoais, agora vou perguntar apenas uma opnião sua: qual sua comida favorita?'.format(nome))
    time.sleep(1.7)
    print('{}, espero que a comida {} seja boa, até porque sou apenas uma máquina e não sou capaz de comer, sentir o gosto ou cheiro de um alimento como os seres vivos, mas tenho muitas informações sobre ele!'.format(nome,comfav))

Nome_apresentacao()