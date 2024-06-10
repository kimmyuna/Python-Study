# 아래 함수가 실행 시 에러가 발생하는 이유를 생각해보세요

#함수 선언
# def greet(msg="Good Morning!", name) :
#     return "Hi!" + name + ', ' + msg

# 실행
# print(greet("Kim"))
# print(greet("Park", "How do you do?"))

# 모든 인자가 디폴트 값
# 모든 인자가 디폴트 값 X
# 디폴트 값 인자가 뒤로

#예제1
def greet(name, msg="Good Morning!") :
    return "Hi!" + name + ', ' + msg

print(f'ex1 결과 : {greet("Kim")}')
print(f'ex1 결과 : {greet("Park", "How do you do?")}')

#예제2
def add1(a, b=10, c = 15) :
    print(a,b,c)
    return a+b+c

print(f'ex2 결과 : {add1(15)}')
print(f'ex2 결과 : {add1(b=100, c=25, a=30)}')

# 예제3
def add2(*d):
    tot = 0
    for i in d :
        tot += i
    return tot

print(f'ex3 결과 : {add2(10, 20, 30)}')
print(f'ex3 결과 : {add2(*(i for i in range(1, 101)))}') #패킹 언패킹