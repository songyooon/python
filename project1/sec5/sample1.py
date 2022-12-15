#지방, 탄수화물, 단백질의 그램을 키보드로 입력하면 칼로리를 계산하여 출력하는 프로그램
#총 칼로리 = 지방*9+단백질*4+탄수화물*4
#총 칼로리(calorie), 단백질(protein), 지방(fat), 탄수화물(carbonhydrate)으로 변수 선언

fat=0
protein=0
carbonhydrate=0
calorie = calorie = fat*9 + protein*4 + carbonhydrate*4

def plus():
    fat=int(input("지방 : "))
    protein=int(input("단백질 : "))
    carbonhydrate=int(input("탄수화물 : "))
    print("총 칼로리 : ", calorie)
