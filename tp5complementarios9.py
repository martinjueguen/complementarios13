print("ingrese cuantos numeros va a ingresar")
c=int(input())
i=int(1)
num=int(0)
max=int(-9999999999)
min=int(9999999999)
for i in range(1,c+1):
    print("ingrese un numero")
    num=int(input())
    if num>max:
        max=num
    if num<min:
        min=num
print("el numero mas chico es",min,"y el mas grande es",max)