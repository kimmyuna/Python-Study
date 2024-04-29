#연습예제 1
#아래 파이썬 코드의 결과 값을 True or False 값을 예상

x=15
y=25


print('예제1 결과')
print(f'x == y : {x == y}')  #False
print(f'x is y : {x is y}')  #False
#is는 변수의 object의 값이 같아야 함


#연습예제2
#아래 파이썬 코드의 결과값을 True or False 값을 예상

x = ['orange', 'banana', 'apple']
y= x

print('예제2 결과')
print(f'x == y : {x == y}')  #True
print(f'x is y : {x is y}')  #True
print(f'x value, id " {x}, {hex(id(x))}')
print(f'y value, id " {y}, {hex(id(y))}')


#연습예제3
#아래 파이썬 코드의 결과값을 True or False 값을 예상
x = ['orange', 'banana', 'apple']
y = ['orange', 'banana', 'apple']

print('예제3 결과')
print(f'x == y : {x == y}')  #True
print(f'x is y : {x is y}')  #False
print(f'x value, id " {x}, {hex(id(x))}')
print(f'y value, id " {y}, {hex(id(y))}')
# x와 y의 값은 같지만 객체가 다름


# is, not is -> 참조, 객체(same object, 오브젝트) 비교
# ==, != -> 값 비교
# 값, 참조가 같은 비교는 is 사용(중요)


#### ** 결과 & 보충설명
a = 15
b= 25

print(a == b) #False
print(a is b) #False


c = []
d = c
e = c+d

print('보충설명 결과')
print(c == d) #True
print(c is d) #True
print(c == e) #True
print(c is e) #True
print(f'c value, id " {c}, {hex(id(c))}')
print(f'e value, id " {e}, {hex(id(e))}')
