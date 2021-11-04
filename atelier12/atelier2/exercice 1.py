l1=[1,25,36,48,56]
l2=[14,25,10,7,98]
l3=[]
for i in range(1,len(l1),2):
    l3.append(l1[i])
for j in range(0,len(l2),2):
    l3.append(l2[j])
    print(l3)

