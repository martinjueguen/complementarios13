print("ingrese la cantidad de empleados")
em=int(input())
i=int(0)
sueldoM=int(-1)
num=int()
for i in range (1,em+1):
    print("ingrese el sueldo del empleado nº",i)
    sueldo=int(input())
    if sueldo>sueldoM:
        sueldoM=sueldo
        num=i
print ("el empleado nº",num,"es el que tiene el sueldo mas alto, cobrando",sueldoM)