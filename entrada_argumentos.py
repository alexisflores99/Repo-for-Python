import sys 
if len(sys.argv)==3:
    texto=sys.argv[1]
    repeticiones = int(sys.argv[2])
    for i in range(repeticiones):
        print(texto)
else:
    print("Error, introdujo uno (1) o más de dos (2) argumentos")