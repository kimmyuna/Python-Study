# 21. String Split By Delimeter
# 아래와 같은 문장을 공백으로 구분 후 단어 개수를 출력하는 함수를 작성 후 실행

#예제 1
txt1 = 'Suppose we have few words that are separated by spaces'

a = txt1.split()

print(a)
print(f'ex1의 결과 : {len(a)}')

#예제2
txt2 = input()

b = txt2.split("&")
print(b)
print(f'ex2 결과 : {b}')

# Python Spit() 함수 사용
# string.split(seperator, maxsplit) : 구분자, 분할 수
# 기본 분리 지정자는 공백
# 문자열을 구분 후 리스트로 변환