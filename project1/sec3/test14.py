
set0 = {60, 90, 80, 70, 90, 60, 100, 80}
lst1 = [0, 0, 0, 0, 0, 0]
set1 ={}
for i in range(6):
    lst1[i]=random.randint(1, 45)
    print(lst1[i])

i=0
while True:
    if(len(set1)<6):
        a=random.randint(1, 45)

set2 = {10, 20, 30, 40}
set3 = {20, 40, 60, 80}
print(type(set2), set2)
set2.add(60)
set3.add(100)
print(set2)
set2.clear()
print(set2)
union1 = set2 | set3
union2 = set2.union(set3)
print(union1)
print(union2)

inter1 = set2 & set3
print(inter1)
minus1 = set2 - set3
print(minus1)

