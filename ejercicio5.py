#1 imprimir cadena
# def cadena(nombre):
#     return nombre

# print(cadena("Alexis"))

#2 validar email
# def validar_email():
#     email = input("Ingrese su email: ")
#     if '@' in email :
#         print("Email correcto")
#     else:
#         print("Email incorrecto")

# validar_email()

#3
# def argu(**kwargs):
#     print(kwargs)

# argu(a="Python",b=True,c=["Hola","Ctm"])

def generarPares(limite):
    num = 1
    lista = []
    while num<limite:
        lista.append(num*2)
        num+=1
    
    return lista

print(generarPares(10))
