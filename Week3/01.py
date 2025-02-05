# FLY-AL-LOGITECH
# [3주차] 2025-02-05
# [문제1] 코딩테스트 연습 > 완전탐색 > 최소직사각형

def solution(sizes):
    sizes = [[max(w, h), min(w, h)] for w, h in sizes]

    max_width = max(w for w, h in sizes)
    max_height = max(h for w, h in sizes)

    return max_width * max_height