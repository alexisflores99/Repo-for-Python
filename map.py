# def doblar(numero):
#     return numero*2

# numeros = [2,5,45,10,36]

# i = map(doblar, numeros)
# print(list(i))

doblar = lambda a,b : a*b

a = [1,2,3,4,5]
b = [6,7,8,9,10]
i = map(doblar,a,b)
print(list(i))