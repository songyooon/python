import random
lst1 = [0,0,0,0,0,0]
for i in range(6):
    lst1[i]=random.randint(1,45)
set1 = set(lst1)
while True:
    if(len(set1)<6):
        a=random.randint(1, 45)
        set1.add(a)
    if(len(set1)==6):
        lst1=list(set1)
        lst1.sort()
        break
print("로또번호 : ",lst1)
