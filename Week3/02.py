# FLY-AL-LOGITECH
# [3주차] 2025-02-05
# [문제2] 코딩테스트 연습 > 정렬 > K번째수


def solution(array, commands):
    result = []
    
    for i, j, k in commands:
        sorted_array = sorted(array[i-1:j])
        result.append(sorted_array[k-1])
    
    return result