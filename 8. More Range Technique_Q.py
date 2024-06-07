#`아래와 같이 1부터 20까지 홀수 * 10, 짝수는 그대로리스트로 출력하세요.

#ex1
ex1 = []
for i in range(1,20):
    if i %2 == 1 :
        ex1.append(i * 10)
    else :
        ex1.append(i)

print(f'ex1의 결과 : {ex1}')

#방법2
ex2 = list ( i*10 if i%2 == 1 
          else i for i in range(1,21,1))

print(f'ex2의 결과 : {ex2}')

#응용(List Comprehension)
print([[j for j in range(5)] for i in range(5)])
##리스트 안에서 리스트를 만들 수 있음


# List Comprehension : 짧은 문법(Syntax)으로 간단하게 조건에 맞는 리스트 생성
# [x for x in list]
# [x for x in list if conditions]
# [ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in list] 