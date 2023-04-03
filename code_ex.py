d=[]
for i in range(0,100,3):
    d.append(i)
print(d)
l=[]
sum1=1
for i in range(100):
    sum1=sum1+i
    l.append(sum1)
print(l)



result=1
l1=[]
l1.append(result)
for i in range(1,100):
    j=3
    res=i*j
    result+=i
    l1.append(res)
    l1.append(result)
print(l1)