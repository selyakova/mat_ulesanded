from random import *
tase=4
oige=0
kogus=0
while tase not in [1,2,3]:
    try:
        tase=int(input("Vali tase:"))
    except TypeError:
        print("Vale tase!")
        
print(f"Sinu valik on {tase}")

#tase 1 +,-, 0,-100
#tase 2 +,-,*,/ -100,100
#tase 3 +,-,*,/,//,%,** -200,200
if tase ==1:
    min_arv=0
    max_arv=100
    tehe_arv=1
    tehed=["+","-"] #tehed[0]="+",tehed[1]="-"
elif tase==2:
    min_arv=-100
    max_arv=100
    tehe_arv=2
    tehed=["+","-","*"]
else:
    min_arv=-200
    max_arv=200
    tehe_arv=3
    tehed=["+","-","*","/"]
print(f"Tasel {tase} arvude vahemik on ({min_arv};{max_arv}) ja tehed on {tehed}")
if tase==1:
    kogus=int(input("Ülesandete arv:"))
    for i in range(1,kogus+1):
        arv1=randint(min_arv,max_arv)
        arv2=randint(min_arv,max_arv)
        tehe=randint(0,tehe_arv) 
        mark=tehed[tehe] 
        print(f"{arv1}{mark}{arv2}=",end="")
        vas=eval(str(arv1)+mark+str(arv2))
        vastus=int(input())
        if vastus==vas: 
            oige+=1
        else:
            print("Õige vastus on",eval(str(arv1)+mark+str(arv2)))       
elif tase==2:
    kogus=int(input("Ülesandete arv:"))
    for i in range(1,kogus+1):
        arv1=randint(min_arv,max_arv)
        arv2=randint(min_arv,max_arv)
        tehe=randint(0,tehe_arv) 
        mark=tehed[tehe] 
        print(f"{arv1}{mark}{arv2}=",end="")
        vas=eval(str(arv1)+mark+str(arv2))
        vastus=int(input())
        if vastus==vas: 
            oige+=1
        else:
            print("Õige vastus on",eval(str(arv1)+mark+str(arv2)))  
elif tase==3:
    kogus=int(input("Ülesandete arv:"))
    for i in range(1,kogus+1):
        arv1=randint(min_arv,max_arv)
        arv2=randint(min_arv,max_arv)
        tehe=randint(0,tehe_arv) 
        mark=tehed[tehe] 
        print(f"{arv1}{mark}{arv2}=",end="")
        vas=eval(str(arv1)+mark+str(arv2))
        vastus=int(input())
        if vastus==vas: 
            oige+=1
        else:
            print("Õige vastus on",eval(str(arv1)+mark+str(arv2)))
if (oige/kogus)*100>=90:
    hinne="5"
elif 75<=(oige/kogus)*100<90:
    hinne="4"
elif 60<=(oige/kogus)*100<75:
    hinne="3"
else:
    hinne="2"
print(f"Kokku oli {kogus} ülenandeid, õigesti oli lahendatud {oige}\nSinu hinne on {hinne}")
