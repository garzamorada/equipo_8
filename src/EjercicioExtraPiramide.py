n = int(input("Ingrese el número"))

if n > 0:
    for i in range(1, n+1):
        print("\n")
        for j in range (1, i+1):
            print(i, end=" ")
else:
    print("El número ingresado no es correcto.")