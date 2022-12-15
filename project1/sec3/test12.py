a=[]
b=["kim", 1004, 6.28, True]
print(id(b), type(b), b)
print(id(b[0]), type(b[0]), b[0])
print(b[1:3])
print(b[1:])
print(b[:3])
print(b[::2])
print(b[::-1])

c=["park", 100, "A", False]
d=b+c
print(d)
comment = "My name, is kitae, kim park, lee, kim, han, park, kang"
e=comment.split(sep=' ')
print(e)
print("kim의 인덱스 : ", e.index('kim'))
print("개수 : ", e.count('park'))
print("전체 원소의 수 : ", len(e))
