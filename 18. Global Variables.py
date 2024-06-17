# 18. Global Variables
# 아래 함수가 실행 시 에러가 발생하는 이유

# 전역변수 : 전체에서 Accsess 할 수 있는 함수

# x = 100

# def test() :
#     x = x * 10
#     return x

# print(test())

# 전역변수 예제1
x = 100

def test1() :
    return x * 10

print(f' ex1의 결과 {test1()}')

# 전역 변수 예제2
y = 100

def test2() :
    global y
    y = y * 10
    return y

print(f' ex2의 결과 {test2()}')


# 파이썬 변수 스코프(영역)에 대한 이해
# 변수 영역에 대한 이해 부족 시 잘못될 결과 값, 프로그램 종료 등 문제 발생
# 전역 변수 : 함수 내부가 아닌 외부에 정의되어 전체 범위를 갖는 변수(프로그램 영역 전체, 내부 엑세스 가능)
# 전역 변수의 변경, 수정(출력, 엑세스 X)이 필요한 경우는 global 키워드 사용