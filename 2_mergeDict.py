l1=int(input("Limit 1 : "))
d1={}
d2={}
for x in range(l1):
    key,value=map(str,input().split())
    d1[key]=value
l2=int(input("Enter l2 : "))
for x in range(l2):
    key,value=map(str,input().split())
    d2[key]=value
print(d1|d2)
