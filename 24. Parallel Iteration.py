# 24. Parallel Iteration
# 아래의 리스트를 {key : a, vlaue : b*c} 형태의 Dict(딕셔너리) 구조로 변경

a = ["one", "two", "Three"]
b = [30, 20, 15, 75]
c = [5.2, 7.4, 3.6, 4.2]

#방법1
result1 = {}
for x, y ,z in zip(a,b,c) :
    result1[x] = y * z

print('ex1 결과 :', result1)

#방법2
print('ex2 결과 :', {x: y * z  for x, y, z in zip(a,b,c)})

#방법3
print('ex3 결과 :', dict((x, y*z) for x, y, z in zip(a,b,c)))


# 다양한 Iterable 그룹을 묶어 연산
# zip : 다중 그룹의 반복가능한 자료형을 묶는 기능
# usage : zip(*iterables, strics=False)
