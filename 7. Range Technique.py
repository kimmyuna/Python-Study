# 다음과 같이 30 ~ -10 까지 -2씩 감소한 결과를 리스트로 출력하세요.`
import this

#방법1
ex1 = []
for i in range(30, -12, -2) :
    ex1.append(i)

print(f'ex1 결과 : {ex1}')


#방법2
ex2 = list(range(30, -12, -2))
print(f'ex2 결과 : {ex2}')

# range 함수(내장) : 주어진 범위 사이의 숫자형 시퀀스 반환
# loop 관점에서 핵심적인 함수(주로 for, while 함께 사용)
# range(stop) takes one argument.
# range(start, stop) takes two arguments.
# range(start, stop, step) takes three arguments.