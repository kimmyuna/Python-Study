#9. Range & Map & Rambda
# 아래와 같이 1부터 15까지 원소 *10 결과는 문자열 리스트로 출력하세요
# range, map, ramda 사용

#방법1 : 제일 기본적인 방법
ex1 = []
for i in range(1,16) :
    ex1.append(str(i * 10))
print(f'ex1 결과 :  {ex1}')

#방법2
ex2 = []
ex2 = list(map(lambda i : str(i *10), range(1,16)))
print(f'ex2 결과 :  {ex2}')

#방법3
print(f'ex3 결과 :  {list(map(lambda x : str(x*10), range(1, 16)))}')

# HINT
# 람다함수 : 인라인 작성으로 인해 가독성 증가(함수 표현식 내용이 적을 때 람다 사용 권장)
#            함수 객체 반환 -> 함수 객체 인수로 받는 map, filter 등과 연계 사용
# lambda : 
## lambda 매개변수 : 표현식
## ex1) Add 10 to argument a, and return the result :
x = lambda a : a + 10
print(x(5))  #결과는 15 출력
## ex2) Multiply argument a with argument b and return the result:
x = lambda a, b :  a * b 
print(x(5,6)) #결과는 30 출력
## ex3) Summarize argument a, b, and c and return the result:
x= lambda a, b, c : a + b + c
print(x(5,6,2)) # 결과는 13출력

# map : 
## map(함수, 리스트)
## 리스트로부터 원소를 하나씩 꺼내서 함수를 적용시킨 다음 그 결과를 새로운 리스트에 담아줌
## ex1)
print(list(map(lambda x: x ** 2, range(5))))

## ex2)
def addition(n):
    return n + n
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))


