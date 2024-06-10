#12. Add Dict Items
# 아래와 같이 Dictionary 예 ['c' : 'banana', 'd' : 'kiwi'] 를 추가하세요.

d = {'a' : 'apple', 'b' : 'grape'}

#  방법1
d['c'] = 'banana'
d['d'] = 'kiwi'


print(f'ex1의 결과 : {d}')

#방법2 : update 함수 -> 없는 키 값은 추가, 있는 키 값은 변경됨1
e = {'a' : 'apple', 'b' : 'grape'}
e.update({'c' : 'banana', 'd' : 'kiwi'})


print(f'ex2의 결과 : {e}')




# 기존 Dict 구조에 새로운 item 추가, 제거는 자주 일어남
# Python Dict에서 Key로 요소의 값에 접근 가능 -> e[key]
# Dict의 Update 함수도 사용