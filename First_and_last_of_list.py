import random
def list_sol(a):
    b=[]
    b.extend([a[0],a[len(a)-1]])
    return b
c =random.sample(range(1,30),12)
print(c)
print(list_sol(c))
    
