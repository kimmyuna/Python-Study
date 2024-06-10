#14. Data Pretty Printer

# 아래와 같이 코드를 작성한 후 실행 Jason 형식을 구조에 맞게 출력(pprint)

from urllib import request
import json

response = request.urlopen("https://Jsonplaceholder.typicdode.com/users")

response_json = response.read()

d= json.loads(response_json)

#출력 결과 비교
print(d)

#출력 결과 비교(pprint)
from pprint import pprint

pprint(d)

# pprint : Python 데이터 구조를 예쁘게 인쇄할 때 사용하는 기능 제공
# depth(중첩 데이터), indent(들여쓰기), width(줄길이 조정), sort_dicts(키 정렬), stream(파일에 출력) 옵션 제공