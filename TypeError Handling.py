#아래 파이썬 코드가 에러(예외)가 발생하는지 생각해보고 동작하도록 수정

#코드
#x = "Seoul"
#y = 25
#z = x + y
#print(f'x+y : {z}')
### x의 타입은 string, y의 타입은 int(숫자형) 이므로 계산 시 타입불일치로 오류가 나타남

#수정
x = "Seoul"
y = 25
z = x + str(y)
print(f'x+y : {z}')

# 문자열 <-> 정수 연산은 형변환(Type Casting)이 필요함
# calling a non-callable인 경우
# 리스트 인덱스 타입 에러인 경우
# 기타 타입 에러