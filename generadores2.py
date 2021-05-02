def devuelvePaises(*paises):
    for elemento in paises:
        yield from elemento

paises_dev = devuelvePaises("Peru","Brasil","Chile")
print(next(paises_dev))
print(next(paises_dev))
print(next(paises_dev))
print(next(paises_dev))