
limit=int(input("Limit : "))
l1=[]
for x in range(limit):
    key,value=list(map(str,input().split()))
    l1.append((key,value))
tup=tuple(l1)
print(dict(tup))
