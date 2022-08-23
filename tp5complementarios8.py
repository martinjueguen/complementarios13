print("ingrese la cantidad de numeros a evaluar")
cant=int(input())
i=int
num=int
con=int(0)
for i in range(1,cant+1):
    print("ingrese el digito")
    num=int(input())
    if num ==0:
        con=con+1

print("La cantidad de 0 es",con)