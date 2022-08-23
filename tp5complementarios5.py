from ast import Mod, mod


print("ingrese un numero")
num=int(input())
i=int(1)
acomulador=int()

for i in range(1,num+1):
    if i%2  == 0:
        acomulador=acomulador-1/i
    else:
        acomulador=acomulador+1/i
print (acomulador)