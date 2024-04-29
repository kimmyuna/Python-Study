# 연습예제1
# 아래 파이썬 코드가 왜 에러(예외)가 발생하는지 생각해보고 동작하도록 수정

# 문자열 <-> 정수 연산은 형변환이 필요함
x = 'Seoul' ##문자형
y = 25  ##숫자형
y = str(25)  #숫자 25를 string형으로 바꿔야 동작함

print('1. 문자열 <-> 정수 연산')
print(f'x + y : {x+y}')

# Calling a non-callable인 경우
etc = "KoreaSeoul"

print('2. caling a non-callable')
print(etc()) # etc는 str타입이지만, 함수형으로 호출을 해서 오류 발생

# 리스트 인덱스 타입 에러인 경우

c = [1,2,3,4,5]
print('3. 리스트 인덱스 타입 에러')
print(c["2"]) #인덱스 번호를 str형태로 넣어서 오류 발생


# # 기타 타입 에러
