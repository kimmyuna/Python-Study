#11. Dict Items Sum

#아래와 같은 Dict 구조에서 모든 value 값의 합(sum)을 구하세요
#딕셔너리 형식 : 키와 값의 구조로 지정된 리스트(데이터를 저장하기 위한 하나의 형태)

d = {'a': 17,'b': 114,'c': 247, 'd': 362, 'e': 220, 'f': 728, 'g': -283, 'h': 922}

#방법1
total = 0
for i in d.values():
    total = total + i
print(d.values())
print(f'ex1 결과 : {total}')

#방법2
print(f'ex2 결과 : {sum(d.values())}')

#방법3
print(f'ex3 결과 : {sum([d[item] for item in d])}')

# 방법4
from functools import reduce

print(f'ex4 결과 : {reduce(lambda x,y:x+y,d.values())}')


# Dict : Key와 value의 대응관계를 갖는 자료형(해시테이블, 가변적-수정가능)

# 자주 사용하는 함수 : get(), values(), keys() 

# 다양한 Dict 선언 방법에 대해서 알아둬야 해요!
# 빈 딕셔너리
d = {}

# 자주 사용
d = {1: 'banana', 2: 'apple'}

# 다양한 키 조합
d = {'name': 'Lee', 1: [5, 6, 7]}

# 직접 선언
d = dict({1:'banana', 2:'apple'})

# 시퀀스형 페어로 선언
d = dict([(1,'banana'), (2,'apple')])