c=int(0)
i=int(1)
num=int(0)
for i in range(1,10):
    print("ingresa un numero")
    num=int(input())
    if num%2==0:
        c=c+1
print("hay",c,"numeros pares")