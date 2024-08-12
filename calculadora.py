def sumar(num1, num2):
    return num1+num2

def restar(num1, num2):
    return num1-num2

def multiplicar(num1, num2):
    return num1*num2

def dividir(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            print("El divisor debe ser distino de 0")
        
            
num1 = int(input("Ingrese primer numero a operar: "))
num2 = int(input("Ingrese segundo numero a operar: "))
num = int(input("Ingrese 1 para sumar, 2 resta, 3 multiplicacion 0 4 division: "))

if num == 1:
    resultado = sumar(num1,num2)
    print(f"El resultado de la suma es: {resultado}")
    
elif num == 2:
    resultado = restar(num1,num2)
    print(f"El resultado de la resta es: {resultado}")

elif num == 3:
    resultado = multiplicar(num1,num2)
    print(f"El resultado de la multiplicacion es: {resultado}")

elif num == 4:
    resultado = multiplicar(num1,num2)
    print(f"El resultado de la division es: {resultado}")

