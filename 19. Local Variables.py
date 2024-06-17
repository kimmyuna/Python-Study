# 19. Local Variables
#아래 함수를 실행 후 Step1, Step2, Step3 결과를 예측해보세요

# a = 20  #전역변수
# def test() :
#     # 지역변수
#     a = 35
#     return a
# print(f'step1 : {a}')

# a = 100

# print(f'step2 : {a}')
# print(f'step3 : {test()}')


a = 20
def test() :
    global a
    print(f'ex3 결과 : {a}')
    a= 35

    return a

print(f'ex1 결과 : {a}')

a = 100

print(f'ex2 결과 : {a}')
print(f'ex4 결과 : {test()}')

print(f'ex5 결과 : {a}')

a = 7777
print(f'ex6 결과 : {a}')