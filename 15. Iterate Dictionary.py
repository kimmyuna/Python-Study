# 15. Iterate Dictionary
# 아래와 같은 딕셔너리를 출력 결과와 같이 완성하세요(반복문 사용)

#Dict 선언
d = dict(one = list(range(1,11)), two = list(range(11,23)), three = list(range(23, 37)))

# 방법1
for k, v in d.items() :
    print(f'key "{k}" has values {v} -> total : {len(v)}')

# Iterator : 순서대로 다음에 값을 반환(리턴) 할 수 있는 객체 또는 상태(자체적으로 next 메소드 내장) 반복가능한 객체, 순회하면서 처리
# Dict구조의 Items(), keys(), get() 함수 기억하기!
