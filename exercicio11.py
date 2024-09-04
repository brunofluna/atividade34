# Crie um programa com funções para calcular a área de 4 figuras geométricas (quadrado, círculo, triângulo e trapézio).
# if __name__== "__main__":
  
def mostrar_menu():
    print('1 - Calcular quadrilátero.')
    print('2 - Calcular triângulo.')
    print('3 - Calcular círculo.')
    print('4 - Calcular Trapézio.')
    print('5 - Sair do Programa.')

def calcular_quadrilatero(b, h):
    result = b * h
    return result

def calcular_triangulo(b, h):
    result = (b * h)/2
    return result

def calcular_circulo(r):
    result = 3.14*(r**2)
    return result

def calcular_trapezio(B, b, h):
    result = ((B + b) * h) / 2.0
    return result

#programa principal
while True:
    mostrar_menu()

    opcao = input('Opção desejada: ')
    match opcao:
        case '1':
            b = str(input('Digite o valor da base: ')).replace(',', '.')
            h = str(input('Digite o valor da altura: ')).replace(',', '.')
            b = float(b)
            h = float(h)
            print(f'Área do quadrilátero: {calcular_quadrilatero(b, h)}.')
            continue
        case '2':
            b = float(input('Digite o valor da base: ').replace(',', '.'))
            h = float(input('Digite o valor da altura: ').replace(',', '.'))
            print(f'Área do triângulo: {calcular_triangulo(b, h)}.')
            continue
        case '3':
            r = float(input('Digite o valor do raio: ').replace(',', '.'))
            print(f'Área do triângulo: {calcular_circulo(r)}.')
            continue
        case '4':
            B = float(input('Digite o valor da base maior: ').replace(',', '.'))
            b = float(input('Digite o valor da base menor: ').replace(',', '.'))
            h = float(input('Digite o valor da altura: ').replace(',', '.'))
            print(f'Área do trapézio: {calcular_trapezio(B, b, h)}.')
            continue
        case '5':
            print('Programa Encerrado.')
            break
        case _:
            print('Opção Inválida!')
            continue

''' método principal
def main():
  # vamos ler a medida da base maior
  b_maior = float(input("Medida da base maior (B): "))
   
  # vamos ler a medida da base menor
  b_menor = float(input("Medida da base menor (b): "))
   
  # vamos ler a medida da altura
  altura = float(input("Medida da altura (h): "))
     
  # e agora calculamos a área do trapézio
  area = ((b_maior + b_menor) * altura) / 2.0
     
  # e mostramos o resultado
  print("A área do trapézio é: {0} cm quadrados.".format(area))
   
if __name__== "__main__":
  main()
  '''