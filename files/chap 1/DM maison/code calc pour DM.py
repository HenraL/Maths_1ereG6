import random
d1=[1,2,2,3,3,4]
d2=[1,3,4,5,6,8]
def Pause():
    i=input("Appuyez sur entrer pour continuer...")
def norm():
    t,X,turn=True,0,0
    while t==True:
        if X==10:
            t=False
            return X
        else:
            dn1=random.randint(1,6)
            dn2=random.randint(1,6)
            X=dn1*dn2
            print("X={}".format(X))
        turn+=1
        print("Jetés={}".format(turn))

def truques():
    t,X,turn=True,0,0
    dMainBel=[]
    dMainEqu=[]
    dMainSup=[]
    dMain=[]
    while t==True:
        if X==10:
            t=False
            return X
        else:
            dn1=d1[random.randint(0,5)]
            dn2=d1[random.randint(0,5)]
            X=dn1*dn2
            dMain.append(X)
            dMain.sort()
            print("X={}".format(X))
            if X<10:
                print("<10")
                dMainBel.append(X)
                if len(dMain)==200:
                    t=False
            elif X==10:
                print("=10")
                dMainEqu.append(X)
                #if len(dMain)==200:
                    #t=False
            elif X>10:
                print(">10")
                dMainSup.append(X)
                #if len(dMain)==200:
                    #t=False
            #elif turn<200:
                #t=False
            #elif len(dMain)<200:
                #t=False
            #elif len(dMainBel)==200:
                #t=False
        turn+=1
        print("Jetés={}".format(turn))
    dMain.sort()
    dMainSup.sort()
    dMainEqu.sort()
    dMainBel.sort()
    print("inféreur à 10")
    print(dMainBel)
    print("égal à 10")
    print(dMainEqu)
    print("suppérieur à 10")
    print(dMainSup)

def possLancDesNorm():
    d1,d2,lanc=0,0,0
    for d1 in range(6):
        d2=0
        for d2 in range(6):
            dMain=(d1+1)*(d2+1)
            lanc+=1
            print("X={} (pour {}*{}) lancé n°{}\n".format(dMain,d1+1,d2+1,lanc))

def possLancDesTruqués():
    d11,d22,lanc=0,0,0
    ddMain=[]
    for d11 in range(6):
        d22=0
        for d22 in range(6):
            dMain=d1[d11]*d2[d22]
            lanc+=1
            print("X={} (pour {}*{}) lancé n°{}\n".format(dMain,d1[d11],d2[d22],lanc))
            if dMain<10:
                print("\a")
                ddMain.append(dMain)
    ddMain.sort()
    print(ddMain)
def nombre_metre(S):
    C=130
    n=1
    while C<S:
        C+=52
        n+=1
    print(n)

print("norm")
norm()
print()
print("possLancDesNorm")
possLancDesNorm()
print()
print("possLancDesTruqués")
possLancDesTruqués()
print()
print("truques")
truques()
print("nombre_metre(116 610)")
nombre_metre(116610)
Pause()
Pause()
