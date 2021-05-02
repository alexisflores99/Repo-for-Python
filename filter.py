edades = [11,15,19,25,14,36,45,12,54,36,22,8]

def mayores(edad):
    return edad>=25


entrar = list(filter(mayores,edades))

print(entrar)