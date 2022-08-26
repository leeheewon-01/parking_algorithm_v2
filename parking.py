def print_list(list):
    for i in range(3):print(list[5-i])  # 3x6 주차지 출력
    print()
    for j in range(3, 6):print(list[5-j])  # 2번째 3x6 주차지 출력

def mid_park(parking, dic, k, l, parking_sucess): # 중간에 주차하는 함수
    if parking[k-1][l] == 0: # 주차장이 비어있으면
        parking[k-1][l] = 1 # 주차장 채우기
        dic[cnt][2][0], dic[cnt][2][1] = k-1, l # 주차장 좌표 저장
        parking_sucess = True # 주차에 성공했다는 것을 알려줌
    elif parking[k+1][l] == 0: # 주차장이 비어있으면
        parking[k+1][l] = 1 # 주차장 채우기
        dic[cnt][2][0], dic[cnt][2][1] = k+1, l # 주차장 좌표 저장
        parking_sucess = True # 주차에 성공했다는 것을 알려줌
    return [parking, dic, parking_sucess] # 주차에 성공했으면 주차장 좌표를 반환하고 아니면 주차장 좌표를 반환하지 않음

dic = [[0,[0,0,0],[-1,-1]] for _ in range(36)] # 주차장 좌표를 저장할 딕셔너리
parking = [[0 for _ in range(6)] for _ in range(6)] # 주차장 상태를 저장할 배열

parking_sucess = False # 주차에 성공했는지 안했는지 확인하는 변수
mid_full = False # 중간에 주차장이 가득 찼는지 확인하는 변수

cnt = 0 # 주차장 순서를 저장할 변수
mid_list = [1, 4] # 중간에 주차할 위치를 저장할 리스트

while True: # 주차장이 가득 찼는지 확인하는 반복문
    car_input = input("차량번호 입력: ") # 차량번호 입력
    out_d, out_h, out_m = map(int, input("출차 시간 입력(d hh mm 형식): ").split()) # 출차 시간 입력

    dic[cnt][0], dic[cnt][1][0], dic[cnt][1][1], dic[cnt][1][2] = car_input, out_d, out_h, out_m # 주차장 정보 저장
    cnt += 1 # 주차장 순서 증가
    for i in mid_list: # 중간에 주차할 위치를 저장한 리스트에서
        for j in range(6): # 주차장의 열을 저장한 반복문
            if parking[i][j] == 0: # 주차장이 비어있으면
                parking[i][j] = 1 # 주차장 채우기
                parking_sucess = True # 주차에 성공했다는 것을 알려줌
                dic[cnt][2][0], dic[cnt][2][1] = i, j # 주차장 좌표 저장
                break 
        if parking_sucess: break # 주차에 성공했으면 반복문 종료
        if i == 4 and j == 5: # 주차장이 모두 가득 찼으면
            mid_full = True # 중간에 주차장이 가득 찼다는 것을 알려줌
            break # 반복문 종료

    if mid_full == True: # 중간에 주차장이 가득 찼으면
        for k in mid_list: # 중간에 주차할 위치를 저장한 리스트에서
            for l in range(6): # 주차장의 열을 저장한 반복문
                for m in range(36): # 주차장의 순서를 저장한 반복문
                    if dic[m][2][0] == k and dic[m][2][1] == l: # 주차장 좌표와 주차장 순서가 같으면
                        if out_d < dic[m][1][0]: # 출차 시간이 주차 시간보다 작으면
                            a = mid_park(parking, dic, k, l, parking_sucess) # 주차장 좌표를 저장할 변수 선언
                            parking, dic, parking_sucess = a[0], a[1], a[2]
                        else: 
                            if out_h < dic[m][1][1]: # 출차 시간이 주차 시간보다 작으면
                                b = mid_park(parking, dic, k, l, parking_sucess) # 주차장 좌표를 저장할 변수 선언
                                parking, dic, parking_sucess = b[0], b[1], b[2]
                            else: 
                                if out_m < dic[m][1][2]: # 출차 시간이 주차 시간보다 작으면
                                    c = mid_park(parking, dic, k, l, parking_sucess) # 주차장 좌표를 저장할 변수 선언
                                    parking, dic, parking_sucess = c[0], c[1], c[2]
                if parking_sucess:
                    break
    print_list(parking)
    parking_sucess = False
