# 20. Local & Global Variables.py
# 아래 함수 실행 후 Step1, Step2 -> a, b, x, y 결과 예측

def test(x, y) :
    global a
    a= 49
    x, y = y, x
    b = 53
    b =7
    a = 135
    # 예상1
    print(f'Step1 : {a}, {b}, {x}, {y}')

a, b, x, y = 8, 13, 33, 44

#함수 실행
test(23, 7)

#예상2
print(f'Step2 : {a}, {b}, {x}, {y}')