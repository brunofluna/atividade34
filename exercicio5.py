# Crie uma lista de 10 nomes (informados dentro do programa). Em seguida, o usuário informa um número inteiro equivalente a um índice, e o programa retorna o nome equivalente ao índice informado pelo usuário.

nomes = ['Bruno', 'Alessandro', 'Daniel', 'Victor', 'Rafael', 'Bruna', 'Alessandra', 'Daniela', 'Vitoria', 'Rafaela']
try:
    ind = int(input('Digite um número de 0 a 10 correspondente ao índice do nome a ser exibido: '))

    print(nomes[ind] if ind >= 0 and ind < 10 else 'Índice inexistente.')
except Exception as e:
    print(f'Não foi possível retornar o nome da lista. {e}.')
    
