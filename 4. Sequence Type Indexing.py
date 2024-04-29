# Sequence : 순서가 있는 데이터의 자료 형태

#연습 예제
# 아래 리스트에서 index 함수를 포함한 방법으로 'Banana' 인덱싱하기

# 직접 접근, index 함수 사용 가능
x = ['Orange', 'Cherry', 'Apple', 'Kiwi', 'Banana', 'Strawberry']

print(x[4])
print('Banana' in x) #바나나가 포함되어있는지 확인
print(x.index('Banana')) #값이 아닌 위치를 가져옴
print(x[x.index('Banana')])

print(x.index('Banana', 0, len(x))) #찾을 길이 지정 가능



# 시퀀스 자료형(데이터의 값이 연속적으로 이루어진 자료구조) : List, Tuple, Str, Range..
# List 관련 함수는 중요!
# cmp, len, max, min, list, append, count, extend, index, insert, pop, remove, reverse, sort..
# index 함수 대소문자 구분
# sort, sorted 함수 차이도 중요