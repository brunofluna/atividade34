# Crie um programa que possua uma lista com números de 1 a 20, e informe quais deles são primos.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def eh_primo(p):
    if p < 2:
        return False
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

primos = []
for numero in numeros:
    if eh_primo(numero):
        primos.append(numero)

print('Os números primos de 1 a 20 são: ', primos)