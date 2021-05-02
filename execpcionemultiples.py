try:
    c = int(input("Ingrese un numero: "))
    c/0
except ValueError:
    print("Error, ese no es un numero mano")
except Exception as c:
    print(type(c).__name__) 