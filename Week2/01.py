# FLY-AL-LOGITECH
# [2주차] 2025-01-22
# [문제1] 코딩테스트 연습 > PCCE 기출문제 > [PCCE 기출문제] 10번 / 공원

def solution(mats, park):

    # 크기순으로 돗자리 정렬
    mats.sort()

    # 돗자리의 최대 크기와 인덱스 초기화
    global max_size
    max_size = 1
    max_index = -1

    # 최대 크기와 인덱스 업데이트 함수
    def update_max_size(mats=mats):
        global max_size
        nonlocal max_index
        # 첫 업데이트인 경우 
        if max_size == 1:
            # 가장 작은 돗자리가 1인 경우
            if mats[0]==1:
                max_size = mats[1]
                max_index = 1
            # 가장 작은 돗자리가 1보다 큰 경우
            else:
                max_size = mats[0]
                max_index = 0
            
            return max_size, max_index
        
        # 이후 업데이트인 경우
        else:
            max_index += 1
            max_size = mats[max_index]
            return max_size, max_index

    # park 배열 bool값으로 만들기
    park_bool = []
    for i in range(len(park)):
        park_bool.append([])
        for j in range(len(park[i])):
            park_bool[i].append(park[i][j]=='-1')

    # 좌표별 돗자리 체크 함수
    def check_mat(x, y, max_size, max_index, park_bool=park_bool, mats=mats):
        # 반복할 횟수 계산
        iter_num = len(mats)-max_index-1

        # 최대값보다 큰 돗자리부터 반복
        for i in range(iter_num):
            # 돗자리 크기 가져오기
            size = mats[len(mats)-iter_num]
            # 돗자리 범위의 모든 좌표 점검
            if y+size>len(park) or x+size>len(park[0]):
                return max_size, max_index

            for b in range(size):
                for a in range(size):
                    # 좌표가 false이면 break하고 기존 최대값 반환
                    if not park_bool[y+b][x+a]:
                        return max_size, max_index
            # 범위 내의 모든 좌표가 true면 최대값 업데이트
            max_size, max_index = update_max_size()
        return max_size, max_index

    # park 배열 순회하며 돗자리 체크하기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park_bool[i][j]:
                max_size, max_index = check_mat(j, i, max_size, max_index)

    return None