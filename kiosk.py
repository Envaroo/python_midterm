# #시네마 키오스크 v0.3
# ages = []
# price = 0
# kids = 0
# mids = 0
# adults = 0
# humans = int(input('몇 분이 오셨습니까?'))
#
# ages = [int(input('나이는?')) for i in range(humans)] #리스트 컴프리헨션
#
# for age in ages:
#     if 0 <= age < 8:
#         price = price + 5000
#         kids = kids + 1
#     elif 8 <= age < 19:
#         price = price + 9000
#         mids =mids + 1
#     elif age >= 19:
#         price = price + 11000
#         adults = adults + 1
#     else:
#         print('정확한 나이를 입력하십시오.')
#
# print("="*50)
# print('총 인원 : {0}명, (어린이 {1}명, 청소년 {2}명, 성인 {3}명)'.format(humans, kids, mids, adults))
# print('총 금액 : {0}원'.format(price))


# # 시네마 키오스크 v0.4
# # Changelog v0.4: 간단한 GUI를 위한 함수를 정의하고, 기본적인 인터페이스를 만들었습니다. 입력 시 오류를 해결하였습니다.
#
# def ui(choice_list):
#     """
#     :param choice_list: 항목에 해당하는 string을 담은 list를 입력받습니다.
#     :return: void
#     :Function: 주어진 양식의 인터페이스를 출력합니다.
#     """
#
#     # 문자열 정렬하기, f-string 사용하기 - 002분반 실습 week3
#     print('=' * 45)
#     for k in range(len(choice_list)):
#         print(f'{choice_list[k]:^30}')
#     print('=' * 45)
#
#
# ages = []
# price = 0
# kids = 0
# mids = 0
# adults = 0
# humans = 0
#
# while True:
#     humans = int(input('몇 분이 오셨습니까?'))
#
#     if humans == 0:
#         print('예매가 취소되었습니다.')
#         break
#
#     elif humans >= 1:
#         break
#
#     else:
#         print('정확한 인원 수를 입력하세요.')
#
#
# if humans >= 1:
#
#     # for i in range(humans):
#     #     age_input = int(input('나이는?'))
#     #     if age_input >= 0:
#     #         ages.append(age_input)
#     #     else:
#     #         print('정확한 나이를 입력해주세요.')
#     #  i 값을 조작하지 못해 사용하지 않기로 함.
#
#     looping = humans - 1
#     while looping >= 0:
#         age_input = input('나이는?')
#         if int(age_input) >= 0:
#             ages.append(int(age_input))
#             looping = looping - 1
#         else:
#             print('정확한 나이를 입력해주세요.')
#
#     for age in ages:
#         if 0 <= age < 8:
#             price = price + 5000
#             kids = kids + 1
#         elif 8 <= age < 19:
#             price = price + 9000
#             mids = mids + 1
#         elif age >= 19:
#             price = price + 11000
#             adults = adults + 1
#
#     ui(['총 인원 : {0}명, (어린이 {1}명, 청소년 {2}명, 성인 {3}명)'.format(humans, kids, mids, adults),
#         '총 금액 : {0}원'.format(price)])


# # 시네마 키오스크 v0.5
# # Changelog
# # v0.4: 간단한 UI를 만들었습니다. 입력 시 오류를 해결하였습니다.
# # v0.5: 예매영화 선택 기능을 추가하였습니다. 예매시간 선택 기능을 추가하였습니다. 모듈화 후 파일을 분리하였습니다.
#
# import tools
#
#
# ages = []
# price = 0
# kids = 0
# mids = 0
# adults = 0
# humans = 0
#
# sel_mov = 0
# sel_time = 0
#
# test_movie = {'name': '1917', 'restriction': 15, 'time': [800, 1200, 1500, 2100]}
# test_movie2 = {'name': '무간도', 'restriction': 12, 'time': [700, 1100, 1300, 2300]}
#
# movies = [test_movie, test_movie2]
# box_office = []
#
# for i in movies:
#     box_office.append(str(movies.index(i) + 1) + '. ' + i['name'] + '  /  ' + str(i['restriction']) + '세 관람가')
#
#
# tools.ui(box_office)
#
# while True:
#     sel_mov = int(input('관람하실 영화를 선택해 주세요: '))
#     if sel_mov <= len(movies):
#         sel_mov = sel_mov - 1
#         # 리스트 인덱스에 맞게 1을 빼줌
#         break
#     else:
#         print('잘못된 입력입니다.')
#
# # sel_mov 의 입력이 끝났습니다
#
# box_time = []
#
# for i in movies[sel_mov]['time']:
#     box_time.append(str(movies[sel_mov]['time'].index(i) + 1) + '. ' + str(i)[0:-2] + ':' + str(i)[-2:])
#
# tools.ui(box_time)
#
# while True:
#     sel_time = int(input('관람하실 시간을 선택해 주세요: '))
#     if sel_time <= len(movies[sel_mov]['time']):
#         sel_time = sel_time - 1
#         # 리스트 인덱스에 맞게 1을 빼줌
#         break
#     else:
#         print('잘못된 입력입니다.')
#
# sel_time 의 입력이 끝났습니다.
#
# humans = tools.humans()
#
# # humans 의 입력이 끝남
#
# if humans >= 1:
#
#     # for i in range(humans):
#     #     age_input = int(input('나이는?'))
#     #     if age_input >= 0:
#     #         ages.append(age_input)
#     #     else:
#     #         print('정확한 나이를 입력해주세요.')
#     #         i = i-1
#     #  ? 작동이 안 됨
#
#     looping = humans - 1
#     while looping >= 0:
#         age_input = input('나이는?')
#         if int(age_input) >= 0:
#             ages.append(int(age_input))
#             looping = looping - 1
#         else:
#             print('정확한 나이를 입력해주세요.')
#
#     for age in ages:
#         if 0 <= age < 8:
#             kids = kids + 1
#         elif 8 <= age < 19:
#             mids = mids + 1
#         elif age >= 19:
#             adults = adults + 1
#
#     price = kids * 5000 + mids * 9000 + adults * 11000
#
# # kids, mids, adults 의 입력이 끝남
#
#     tools.ui(['총 인원 : {0}명, (어린이 {1}명, 청소년 {2}명, 성인 {3}명)'.format(humans, kids, mids, adults),
#               '총 금액 : {0}원'.format(price)])


# # 시네마 키오스크 v0.6
# # Changelog
# # v0.4: 간단한 UI를 만들었습니다. 입력 시 오류를 해결하였습니다.
# # v0.5: 예매영화 선택 기능을 추가하였습니다. 예매시간 선택 기능을 추가하였습니다. 모듈화 후 파일을 분리하였습니다.
# # v0.6: 연령 제한을 설정하였습니다. 시간대별 가격 책정. 모듈화 후 파일을 분리하였습니다. 전체 프로그램을 루프에 넣었습니다.
#
# import tools
#
# while True:
#     price = 0
#     humans = 0
#
#     sel_mov = 0
#     sel_time = 0
#
#     inp = ''
#
#     tools.ui(['1. 영화 예매', '2. 프로그램 종료'])
#
#     while True:
#         inp = input('원하시는 메뉴를 선택해 주세요: ')
#         if inp != '1' and inp != '2':
#             print('잘못된 입력입니다.')
#         if inp == '1' or inp == '2':
#             break
#
#     if inp == '2':
#         print('프로그램을 종료합니다.')
#         break
#
#     test_movie = {'name': '1917', 'restriction': 15, 'time': [800, 1200, 1500, 2100]}
#     test_movie2 = {'name': '무간도', 'restriction': 12, 'time': [700, 1100, 1300, 2300]}
#
#     movies = [test_movie, test_movie2]
#
#     sel_mov = tools.select_movie(movies)
#
#     # sel_mov 의 입력이 끝났습니다
#
#     sel_time = tools.select_time(movies, sel_mov)
#
#     # sel_time 의 입력이 끝났습니다.
#
#     humans = tools.humans()
#
#     # humans 의 입력이 끝남
#
#     age_info = tools.age_set(humans)
#
#     kids = age_info['kids']
#     mids = age_info['mids8'] + age_info['mids12'] + age_info['mids15']
#     adults = age_info['adults']
#
#     restriction_pass = tools.is_pass(movies, sel_mov, age_info)
#     if restriction_pass == 0:
#         input('초기 화면으로 돌아갑니다. (아무 키로 계속하기)\n')
#         continue
#
#     # 연령확인 끝
#
#     tools.receipt(movies, sel_mov, sel_time, humans, age_info, restriction_pass)
#     print('예매표를 확인 해 주세요.')
#     input('\n사용해 주셔서 감사합니다. 초기 화면으로 돌아갑니다. (아무 키로 계속하기)\n')


# 시네마 키오스크 v0.7
# Changelog
# v0.4: 간단한 UI를 만들었습니다. 입력 시 오류를 해결하였습니다.
# v0.5: 예매영화 선택 기능을 추가하였습니다. 예매시간 선택 기능을 추가하였습니다. 모듈화 후 파일을 분리하였습니다.
# v0.6: 연령 제한을 설정. 시간대별 가격 책정. 모듈화 후 파일분리. 전체 프로그램을 루프에 넣었습니다.
# v0.7: 영화 정보를 txt 파일로 입출력합니다. 예매표를 txt 로 출력합니다.
#       좌석 선택 기능을 추가했습니다.
#       좌석의 예약 현황을 #과 .으로 표시하는 함수 show_hall 을 이용합니다.
#       8세 이상 관람가를 삭제했습니다 (실제로 없음), 전연령 관람가를 추가했습니다.
#       ui를 수정했습니다.
#       알파벳 입력이 필요한 부분에서 소문자를 대문자로 처리합니다.
#       파일을 입출력할때 if 문이 아닌 파일 이름 포맷을 통해 입출력합니다.

import tools

while True:
    price = 0
    humans = 0

    sel_mov = 0
    sel_time = 0

    inp = ''

    tools.ui(['1. 영화 예매', '2. 프로그램 종료'])

    while True:
        inp = input('원하시는 메뉴를 선택해 주세요: ')
        if inp != '1' and inp != '2' and inp != '0':
            print('잘못된 입력입니다.')
        if inp == '1' or inp == '2' or inp == '0':
            break

    if inp == '2':
        print('프로그램을 종료합니다.')
        break

    movie_file = open('movie.txt', 'r', encoding='utf8')
    # 영화 파일의 포맷은...
    # name/restriction(0,12,15,18)/timetable/hhmm/hhmm/hhmm.../timeend/hall(A,B)/
    # ex) 1917/15/timetable/800/1200/1500/2100/timeend/A/
    # 004분반 7주차 UTF8 인코딩 사용하기
    mov_lines = movie_file.readlines()
    movies = []
    if mov_lines[-1] == '\n':
        del mov_lines[-1]

    for i in mov_lines:
        mov_detail_lines = i.split('/')
        mov_dict = {'name': mov_detail_lines[0], 'restriction': int(mov_detail_lines[1]),
                    'time': [int(i) for i in mov_detail_lines[3:mov_detail_lines.index('timeend')]],
                    'hall': mov_detail_lines[mov_detail_lines.index('timeend') + 1]}
        movies.append(mov_dict)

    # 영화 정보를 담는 movies 리스트
    # 형식은 [{이름, 연령, [시간], 상영관},{...},{...}]

    movie_file.close()

    # 영화 정보 가져오기... movies 리스트의 입력이 끝났습니다.

    for k in movies:
        for i in k['time']:
            check_time_files = open(f"hall_{k['hall']}{str(i)}.txt", 'a')
            check_time_files.close()

    # check_time_files 는 각 시간대 관객정보를 담은 txt 파일들을 생성합니다.

    sel_mov = tools.select_movie(movies)

    # sel_mov 의 입력이 끝났습니다

    sel_time = tools.select_time(movies, sel_mov)

    # sel_time 의 입력이 끝났습니다.

    humans = tools.humans()

    # humans 의 입력이 끝남

    age_info = tools.age_set(humans)

    kids = age_info['kids']
    mids = age_info['mids12'] + age_info['mids15']
    adults = age_info['adults']

    restriction_pass = tools.is_pass(movies, sel_mov, age_info)
    if restriction_pass == 0:
        input('초기 화면으로 돌아갑니다. (엔터로 계속하기)\n')
        continue

    # 연령확인 끝, 실패하면 전부 continue

    A = [6, 15]
    B = [7, 20]

    # A관과 B관의 좌석정보를 담음

    line = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']

    # 좌석 A열, B열... 표시할때 쓰이는 알파벳 집합
    # ASCII 사용을 검토?

    sel_hall = []

    if movies[sel_mov]['hall'] == 'A':
        sel_hall = A
    elif movies[sel_mov]['hall'] == 'B':
        sel_hall = B

    # sel_hall 에는 상영관의 가로세로좌석 개수가 리스트로 들어감

    sel_seat = []

    # 예매권에 들어갈 좌석정보를 받습니다.

    for i in range(humans):
        occupied_seats = tools.show_hall(sel_hall, movies[sel_mov]['hall'], movies[sel_mov]['time'][sel_time])
        # show_hall() 함수로 표시하고 예약좌석 정보를 받습니다.
        while True:

            # if movies[sel_mov]['hall'] == 'A':
            #     write_seat = open('hall_A{}.txt'.format(movies[sel_mov]['time'][sel_time]), 'a')
            # elif movies[sel_mov]['hall'] == 'B':
            #     write_seat = open('hall_B{}.txt'.format(movies[sel_mov]['time'][sel_time]), 'a')

            write_seat = open(f"hall_{movies[sel_mov]['hall']}{movies[sel_mov]['time'][sel_time]}.txt", 'a')
            # 매 회차 파일을 읽도록...

            while True:
                alpha_inp = input('{}번째 관객분의 열을 선택해 주세요 (알파벳): '.format(i + 1))
                end = sel_hall[0]
                if alpha_inp.upper() in line[0:end]:
                    sel_line = line.index(alpha_inp.upper())
                    break
                else:
                    print('정확한 알파벳을 입력해 주세요.')

            while True:

                sel_row = int(input('{}번째 관객분의 좌석번호를 선택해 주세요 (숫자): '.format(i + 1))) - 1
                if 0 < sel_row < sel_hall[1]:
                    break
                else:
                    print('정확한 좌석을 입력해 주세요.')

            if [str(sel_line), str(sel_row + 1)] in occupied_seats:
                # print([str(sel_line), str(sel_row + 1)])
                # # 테스트전용
                print('이미 선택된 좌석입니다.')
                continue
            else:
                # print(f'{sel_line}, {sel_row}')
                # # 테스트전용
                print('지정했습니다.')
                sel_seat.append([alpha_inp.upper(), sel_row + 1])
                occupied_seats.append([sel_line, sel_row])
                write_seat.write('{0},{1}\n'.format(sel_line, sel_row + 1))
                write_seat.close()
                # 저장하는 형식은 1,5\n
                # 저장할 때는 좌석번호를 알아보기 쉽게 +1 한다.
                break

    # 좌석설정 끝

    seat_info = ''
    for i in range(len(sel_seat)):
        seat_info = seat_info + '{0}열 {1}번째'.format(sel_seat[i][0], sel_seat[i][1]) + '\n'

    # 예매정보에 출력할 좌석정보 저장 끝

    rec_info = tools.receipt(movies, sel_mov, sel_time, age_info)
    print(seat_info + '=' * 45)

    # rec_info 에 좌석정보 X

    # 예매정보 출력

    while True:
        is_print = input('예매표를 출력하시겠습니까? (Y/N)')
        if is_print.upper() == 'Y':
            rec_file = open('receipt.txt', 'w', encoding='utf8')
            rec_file.write(
                '{0}\n{1}관\n{2}\n상영 시작 시간: {3}\n\n<영수증>\n{4}\n{5}\n{6}'.format(
                    movies[sel_mov]['name'],
                    movies[sel_mov]['hall'],
                    seat_info,
                    str(movies[sel_mov]['time'][sel_time])[0:-2]
                    + ':' +
                    str(movies[sel_mov]['time'][sel_time])[-2:],
                    rec_info[0],
                    rec_info[1],
                    rec_info[2]))
            rec_file.close()
            print('예매표가 receipt.txt에 저장되었습니다.')
            break
        elif is_print.upper() == 'N':
            break
        else:
            print('잘못된 입력입니다.')

    input('\n사용해 주셔서 감사합니다. 초기 화면으로 돌아갑니다. (엔터로 계속하기)\n')

