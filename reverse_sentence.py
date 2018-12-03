def reverse(s):
    a=s.split()
    j=[]
    for i in range(len(a)-1,-1,-1):
        j.append(a[i])
    return j

st=str(input("Enter a sentence:: "))
print(" ".join(reverse(st)))
