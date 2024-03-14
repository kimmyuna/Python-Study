#2. 아래 파이썬 코드의 결과 값을 예상하시오
x=15
y=25

print(f'x == y : : {x==y}') #False
print(f'x is y : {x is y}') #False

a = ['orange', 'banana','apple']
b = a

print(f'a == b : {a==b}') #True
print(f'a is b : {a is b}') #True


k = ['orange', 'banana','apple']
l = ['orange', 'banana','apple']

print(f'k == l : {k==l}') #True
print(f'k is l : {k is l}') #False


# is, not is -> 참조, 객체(same object) 비교
# ==, != -> 값 비교
# 값, 참조가 같은 비교는 is 사용(중요)