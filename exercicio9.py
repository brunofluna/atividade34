# Crie um programa onde o usuário cadastre uma quantidade desejada de eventos (nome do evento e classificação indicativa) e após o cadastro dos eventos, o usuário possa informar o nome e a idade, e se inscrever em um dos eventos. Caso o usuário não tenha idade mínima, o programa proíbe a inscrição e pede para o mesmo se inscrever em outro evento. Caso o usuário tenha a idade mínima, o programa inscreve o usuário exibindo a data da inscrição e encerra.

import os
from datetime import date

eventos = []
dia = date.today().day
mes = date.today().month
ano = date.today().year

while True:
    opcao = input('1 para cadastrar evento ou 2 para se inscrever: ')
    os.system('cls')
    match opcao:
        case '1':
            evento = {}
            try:
                evento['nome'] = input('Informe o nome do evento: ')
                evento['censura'] = int(input('Informe a classificação indicativa do evento: '))
                eventos.append(evento)
                print('Evento cadastrado com sucesso.')
            except Exception as e:
                print(f'Não foi possível cadastrar evento. {e}.')
                continue
        case '2':
            nome = input('Informe seu nome')


