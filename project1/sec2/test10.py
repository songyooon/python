data = [90,80,100,60,70]
a=tot=0
for i in data:
    a+=1
    tot+=i
    print("점수 : ", i)
print("총점 : ", tot)
print("평균 : ", float(tot / a))

jum = [(100,80,70),(90,100,80),(80,90,60),(90,100,100)]
for (kor, eng, mat) in jum:
    tot = kor+eng+mat
    avg = float(tot / 3)
    hak = ""
    if(avg>=90):
        hak = "A"
    elif(avg>=80):
        hak = "B"
    elif(avg>=70):
        hak = "C"
    elif(avg>=60):
        hak = "D"
    else:
        hak = "F"

print("학점 : ", hak)

tot=0
for i in range(1,101):
    tot+=i
print("1~100 합계 : ",tot)

data1 = [40,65,70,90,85]
data2 = [num * 2 for num in data1]
data3 = [num * 2 for num in data1 if num%2==0]
print(data2)
print(data3)