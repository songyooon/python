'''
test1.py
'''

print("Hello World~!") # 파이썬 테스트 코드
a = 100 #정수형 변수
b = 6.28 #실수형 변수
c = True #논리형 변수
d = 'kim' #문자열 변수
#여러줄의 문장 데이터 변수
e = '''여러 줄의 
텍스트 
문장'''
#파이썬은 문자열과 숫자를 더할 수 없음
#id(변수명) : 해당 변수의 메모리 주소 구하기
#type(변수명): 해당 변수의 데이터 타입 구하기
print("a=", a, "주소 : ", id(a), type(a)) 
print("b=", b, "주소 : ", id(b), type(b))
print("c=", c, "주소 : ", id(c), type(c))
print("d=", d, "주소 : ", id(d), type(d))
print("e=", e, "주소 : ", id(e), type(e))

