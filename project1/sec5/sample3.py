#항공사의 화물요금을 계산하는 프로그램을 작성하여라
#화물의 10kg 단위당 2,000원이 부과되며, 10kg 미만이면, 화물료는 없음


load=0
fee=0

for(load>=10, fee = load/10*2000)
    for(load<10, fee=0)
print("화물료 : ", fee)