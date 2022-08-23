i=1
cont=0
for i in range(1,20):
    print("ingrese un numero")
    num=int(input())
    if (num%2==0):
        cont=cont+1
print("los numeros pares son",cont)