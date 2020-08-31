import math
def algo(a,b,c):
    delta=b*b-4*a*c
    if delta==0:
        x1=-b/(2*a)
        return x1
    elif delta>0:
        rac=math.sqrt(delta)
        x1=(-b-rac)/(2*a)
        x2=(-b+rac)/(2*a)
        return x1,x2
    else:
        return "pas de solution"
print (algo(2,6,4))
