# 13. Dictionary Data filterting
# 아래와 같은 딕셔너리 구조에서 Value 값이 25이상 필터링 후 출력

d = { 'a' : 8, 'b' : 33, 'c' : 15, 'd' : 26, 'e' : 12, 'f' : 120}

# 방법1
ex1 = {}

for k, v in d.items() :
    if v >= 25 :
        ex1[k] = v

print(f'ex1의 결과 : {ex1}')


#  방법2
ex2 = {k: v for k, v in d.items() if v >= 20}

#dict(((k, v) for k,v in d.items() if >= 20))
print(f'ex2의 결과 : {ex2}')

#  방법3 : 람다 필터 함수 사용
ex3 = dict(filter(lambda v : v[1] >= 25, d.items()))
print(f'ex3의 결과 : {ex3}')


# Dict 필터링 경우 : Key, Value 둘 다 필터링 가능
# Filter 함수 사용
# Dict Comprehension으로 처리 가능
# {조건 만족 시 출력 값 IF 조건 ELSE 조건 불만족 시 출력 값 for i in dict}