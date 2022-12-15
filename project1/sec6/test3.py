protein = int(input('단백질 :'))
fat = int(input('지방 :'))
carbohydrate = int(input('탄수화물 :'))
calorie = fat * 9 + protein * 4 + carbohydrate * 4
print("총 칼로리 :", calorie)

class Calorie:
    calorie = 0

    def inputCalorie(self, p, f, c):
        self.protein = p
        self.fat = f
        self.carbohydrate = c

    def calcCalorie(self):
        return (self.fat * 9 + self.protein * 4 + self.carbohydrate * 4)

p1 = int(input('단백질 :'))
f1 = int(input('지방 :'))
c1 = int(input('탄수화물 :'))
cal = Calorie()
cal.inputCalorie(p1, f1, c1)
calorie = cal.calcCalorie()
print("총 칼로리 :", calorie)

