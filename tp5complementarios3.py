from re import A



A =int()
co=int()
i=1
b=2
for i in range(1,29):
    co=0
    for A in range (2,b//2):
        if b % A == 0:
            co=co+1
            A=b
    if co==0:
        print("El cubo de",b,"es",b**3)
    b=b+1
