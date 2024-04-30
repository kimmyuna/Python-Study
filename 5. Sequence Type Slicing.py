#아래 리스트(List)에서 슬라이싱을 사용해서 [e,f,g] 값을 출력


x = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]

print(x[4:7])
print(x[-9:-6])
print(x[4:-6])
print(x[-9:7])

print(x[6:3:-1]) #역순 출력
print(list(reversed(x[6:3:-1]))) #순서 바꾸기



# 시퀀스 자료형(데이터의 값이 연속적으로 이루어진 자료구조) : List, Tuple, Str, Range..
# List slicing : L[start:stop:step]
# 파이썬 언어 활용 극대화를 위해 리스트 자료구조는 매우 중요
# 시간 복잡도 참고 : https://wayhome25.github.io/python/2017/06/14/time-complexity/