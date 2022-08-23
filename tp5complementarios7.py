print("Ingrese un número:")
num = int( input())
con = 0
for i in range(2, num):
    if num % i == 0:
     con = con + 1

if con == 0:
    print (num, " Es un número primo")
else:
    print (num, " No es un número primo")

