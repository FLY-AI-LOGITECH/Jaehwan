# FLY-AL-LOGITECH
# [1주차] 2025-01-15 
# [문제2] 코딩테스트 연습 > 연습문제 > 짝수와 홀수

def solution(arr):
    answer = []
    init = -1
    
    for num in arr:
        if init != num:
            answer.append(num)
            init = num
            
    return answer