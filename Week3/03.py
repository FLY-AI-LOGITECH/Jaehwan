# FLY-AL-LOGITECH
# [3주차] 2025-02-05
# [문제3] 코딩테스트 연습 > 2021 카카오 채용연계형 인턴십 > 숫자 문자열과 영단어

def solution(s):
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    
    result = ""
    temp = ""

    for char in s:
        if char.isdigit():
            result += char
        else:
            temp += char
            if temp in num_dict:
                result += num_dict[temp]
                temp = ""

    return int(result)