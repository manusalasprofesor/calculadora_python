'''
calculadora_simple.py
Autor: Manu Plaza
Descripción: Calculadora básica en Python
Fecha: 28/10/2025
'''
def sumar(a,b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división entre cero"
    else:
        return a / b

def potencia(a, b):
    return a ** b

def main():
    print('Calculadora simple')
    x = float(input('Introduce el primer número: '))
    y = float(input('Introduce el segundo número: '))

    print(f'Suma: {sumar(x,y)}')
    print(f'Resta: {restar(x,y)}')
    print(f'Multiplicación: {multiplicar(x,y)}')
    print(f'División: {dividir(x,y)}')
    print(f'Potencia: {potencia(x,y)}')

if __name__ == '__main__':
    main()
