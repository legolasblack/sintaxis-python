def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplicar(num1, num2):
    return num1*num2

def dividir(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        return 'Operación erronea'
    

print(dividir(5, 0))

#vamos a aumentar la palabra finally dentro del exception

def dividirFanally(num1, num2):
    try:
        num1=int(num1)
        num2=int(num2)

        print(num1/num2)

    except ValueError:
        print('Los valores introducidos no son correctos')
    
    finally:

        print('calculo finalizado')

dividirFanally("5", "10")
dividirFanally("5", "string")

