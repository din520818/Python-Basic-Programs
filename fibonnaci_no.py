l=int(input("Enter how many fibonnaci numbers you want to print:: "))
a=[1,1]
for i in range(1,l-1):
    a.append(a[i]+a[i-1])
print(a)
