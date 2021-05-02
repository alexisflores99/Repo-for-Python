def suma(num1,num2):
    return num1+num2

def resta(num1,num2):
    return num1-num2

def multiplicar(num1,num2):
    return num1*num2

def division(num1,num2):
    return num1/num2

op1 = int(input("Introduce el primer numero: "))

op2 = int(input("Introduce el segundo numero: "))

operacion = input("Introduce la operación básica pajin: ")

if operacion == "suma":
    print(suma(op1,op2))
elif operacion == "resta":
    print(resta(op1,op2))
elif operacion == "multiplicar":
    print(multiplicar(op1,op2))
elif operacion == "division":
    try:
        print(division(op1,op2))
    except ZeroDivisionError:
        print("No se puede hacer eso en una division mano, en qué estás?")
else: 
    print("Que chucha?")
