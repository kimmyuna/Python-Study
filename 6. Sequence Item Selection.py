#6. Sequence Item Selection
# 아래 리스트(List)에서 apple, kiwi를 추출해서 대문자 리스트로 출력하세요.

x = ["grapes", "mango", "orange", "peach", "apple", "lime", "banana", "cherry", "tomato", "kiwi", "blueberry", "watermelon"]

#방법1
ex1 = []
for i in range(len(x)) :
    if x[i] == 'apple' or x[i] == 'kiwi' :
        ex1.append(x[i].upper())

print(f'ex1 결과: {ex1}')

#방법2 - 람다식
ex2 = list(map(lambda b : b.upper(), filter(lambda a : a == 'apple' or a == 'kiwi', x))) #filter 오브젝트
print(f'ex2 결과: {ex2}')


#방법3 - 리스트 컴프리헨션
ex3 = [a.upper() for a in x if a == 'apple' or a == 'kiwi']
print(f'ex3 결과: {ex3}')


# 파이썬에서 사용가능한 반복문(for, while)은 기억하시죠? -> (break, continue) 필수 기억!
# 시퀀스 자료형(데이터의 값이 연속적으로 이루어진 자료구조) : List, Tuple, Str, Range..
# filter(f, iterable) 함수는 정말 많이 사용해요.(map 함수도 중요!)
# lambda expression(형식)은 다른 함수의 인수 전달 형태로 사용해요.