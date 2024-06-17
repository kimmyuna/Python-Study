#22. String Split By Delimiter(Advanced)
# /source 폴더의 22-1.txt 파일을 공백 구분 후 단어 개수를 출력하는 함수를 작성 후 실행
# 콤마의 경우 두 단어로 취급

txt1 = '/Users/myuna/Python Study/python_basic_1.5/2.QnA/source/22-1.txt'

#방법1
def cnt_word1(filepath) :
    with open(filepath, 'r') as file :
        txt = file.read()
    txt = txt.replace(",", " ")

    #쉼표 제거 확인
    print(txt)

    txt_list = txt.split(" ")
    #리스트 변환(공백)
    print(txt_list)

    return len(txt_list)

print(f'ex1 결과 : {cnt_word1(txt1)}')


#방법2 _ 정규표현식
import re
def cnt_word2(filepath) :
    with open(filepath, 'r') as file :
        txt2 = file.read()

    txt_list2 = re.split(" |,", txt2)

    print(txt_list2)
    return len(txt_list2)

print(f'ex2 결과 : {cnt_word2(txt1)}')



# string.replace(oldvalue, newvalue, count): 타겟, 변환 값, 개수
# 콤마를 공백으로 치환 -> 문자열을 구분 후 리스트로 변환
# python re(Regular Expression) 사용 가능(정규표현식)