#10. Remove Duplicates
# 아래 리스트에서 중복되는 원소를 제거 후 출력하세요
x = ["a", 1, "b", 2, "a", 3, "b", 4, 5, "b"]

#방법1
ex1 = list(set(x))
print(f'ex1 결과 : {ex1}')

#방법2(순서 유지)
from collections import OrderedDict
ex2 = list(OrderedDict.fromkeys(x))
print(f'ex2 결과 : {ex2}')

#방법3(순서유지)
ex3 = []
for i in x :
    if i not in ex3 :
        ex3.append(i)

print(f'ex3 결과 : {ex3}')


# Set(집합 자료형) : 중복 허용 하지 않음, 순서 없음
# List, Tuple : 순서 있음, 중복 허용
# OrderedDict : Dict 순서 보장 받을 수 있음(python 3.6 부터는 기본값)








