def ui(contexts):
    """
    주어진 양식의 인터페이스를 출력합니다.
    :param contexts: 항목에 해당하는 string 을 담은 list
    :return: void

    """

    # 문자열 정렬하기, f-string 사용하기 - 002분반 실습 week3\
    print('=' * 45)
    for k in range(len(contexts)):
        print(f'{contexts[k]:<30}')
    print('=' * 45)


def humans() -> int:
    """
    전체 인원 수를 묻습니다.
    :return: int 타입 인원 수 humans
    """

    while True:
        humans = int(input('몇 분이 오셨습니까?'))
        if humans >= 1:
            return humans

        else:
            print('정확한 인원 수를 입력하세요.')


def age_set(humans) -> dict:
    """
    관객 수에 해당하는 연령 정보를 받고 dict 타입으로 반환합니다.
    :param humans: int 타입 관객 수
    :return: 관객들의 연령 정보를 담은 dict
    """

    ages = []
    age_info = {'kids': 0, 'mids12': 0, 'mids15': 0, 'adults': 0}

    looping = humans - 1
    while looping >= 0:
        age_input = input('나이는?')
        if int(age_input) >= 0:
            ages.append(int(age_input))
            looping = looping - 1
        else:
            print('정확한 나이를 입력해주세요.')

    for age in ages:
        if 0 <= age < 12:
            age_info['kids'] += 1
        elif 12 <= age < 15:
            age_info['mids12'] += 1
        elif 15 <= age < 18:
            age_info['mids15'] += 1
        elif age >= 18:
            age_info['adults'] += 1

    return age_info


def select_movie(movies) -> int:
    """
    영화를 선택합니다.
    :param movies: 영화 정보를 담은 list
    :return: 선택한 영화의 index 값 int
    """
    box_office = []

    for i in movies:
        index_number = str(movies.index(i) + 1)
        movie_name = i['name']
        if i['restriction'] != 0:
            age_restrict = str(i['restriction']) + '세 관람가 '
        elif i['restriction'] == 0:
            age_restrict = '전체 이용가'
        which_hall = str(i['hall']) + '관'

        # if i['restriction'] != 0:
        #     box_office.append(
        #         str(movies.index(i) + 1) + '. ' + i['name']
        #         + '  /  '
        #         + str(i['restriction']) + '세 관람가 '
        #         + str(i['hall']) + '관')
        # elif i['restriction'] == 0:
        #     box_office.append(
        #         str(movies.index(i) + 1) + '. ' +
        #         + '  /  '
        #         + '전체 이용가 '
        #         + str(i['hall']) + '관')

        box_office.append(f"{index_number}. {movie_name:^10} / {age_restrict:^10} / {which_hall}")

    ui(box_office)

    # 영화 목록 표시 끝

    while True:

        sel_mov = int(input('관람하실 영화를 선택해 주세요: '))
        if sel_mov in range(len(movies)+1):
            sel_mov = sel_mov - 1
            # 리스트 인덱스에 맞게 1을 빼줌
            return sel_mov
        else:
            print('잘못된 입력입니다.')


def select_time(movies, sel_mov) -> int:
    """
    시간대를 선택합니다.
    :param movies: 영화 정보를 담은 list
    :param sel_mov: 선택한 영화의 index 값 int
    :return: 선택한 시간대의 index 값 int
    """
    box_time = []

    for i in movies[sel_mov]['time']:
        time_index = str(movies[sel_mov]['time'].index(i) + 1)
        occupy_file = open(f"hall_{movies[sel_mov]['hall']}{str(i)}.txt", 'r')
        occupy_line = occupy_file.read()
        occupy_element = occupy_line.split('\n')
        if occupy_element[-1] == '':
            del occupy_element[-1]
        occ_seats = len(occupy_element)
        if movies[sel_mov]['hall'] == 'A':
            totl_seats = 90
        if movies[sel_mov]['hall'] == 'B':
            totl_seats = 140

        time_format = f"{str(i)[0:-2]}:{str(i)[-2:]}"

        box_time.append(f"{time_index}. {time_format:>6}    {occ_seats} / {totl_seats}")

    ui(box_time)

    while True:

        sel_time = int(input('관람하실 시간을 선택해 주세요: '))
        if sel_time in range(len(movies[sel_mov]['time'])+1):
            sel_time = sel_time - 1
            # 리스트 인덱스에 맞게 1을 빼줌
            if movies[sel_mov]['time'][sel_time] <= 1000:
                print('\n조조 시간대입니다. 가격이 50% 할인됩니다.\n')
            if movies[sel_mov]['time'][sel_time] >= 2200:
                print('\n야간 시간대입니다. 가격이 50% 할인됩니다.\n')
            return sel_time
        else:
            print('잘못된 입력입니다.')


def is_pass(movies, sel_mov, age_info) -> bool:
    """
    연령 정보를 바탕으로 시청 가능, 불가를 판단합니다.
    :param movies: 영화 정보 list
    :param sel_mov: 선택한 영화 int
    :param age_info:
    :return: 시청 가능, 불가를 의미하는 bool
    """

    kids = age_info['kids']
    mids = age_info['mids12'] + age_info['mids15']
    adults = age_info['adults']

    # 연령 정보를 바탕으로 아동, 청소년, 성인 판단

    restriction_pass = 1

    # 기본값은 1

    if movies[sel_mov]['restriction'] == 18:
        if mids >= 1 or kids >= 1:
            restriction_pass = 0
            print('미성년자와 어린이는 관람하실 수 없습니다.')

    if movies[sel_mov]['restriction'] == 15:
        if adults >= 1:
            restriction_pass = 1
        elif kids >= 1 or age_info['mids12'] >= 1:
            restriction_pass = 0
            print('성인의 동행 없이는 관람하실 수 없습니다.')

    if movies[sel_mov]['restriction'] == 12:
        if adults >= 1:
            restriction_pass = 1
        elif kids >= 1:
            restriction_pass = 0
            print('성인의 동행 없이는 관람하실 수 없습니다.')

    return restriction_pass


def receipt(movies, sel_mov, sel_time, age_info):
    """
    가격을 계산하고 영수증을 출력합니다. 예매 정보를 리턴
    :param movies: 영화들의 list
    :param sel_mov: 선택한 영화 index 의 int 값
    :param sel_time: 선택한 영화 index 의, 시간대의 int 값
    :param age_info: 연령 정보를 담은 dict
    :return: 예매 정보를 담은 list
    """

    kids = age_info['kids']
    mids = age_info['mids12'] + age_info['mids15']
    adults = age_info['adults']

    price = kids * 5000 + mids * 9000 + adults * 11000

    is_discount = ''
    if movies[sel_mov]['time'][sel_time] <= 1000 or movies[sel_mov]['time'][sel_time] >= 2200:
        price = price * 0.5
        is_discount = '\n50% 할인'

    rec_info = ['총 인원 : {0}명, (어린이 {1}명, 청소년 {2}명, 성인 {3}명)'.format(kids+mids+adults, kids, mids, adults),
                is_discount,
                '총 금액 : {0}원'.format(int(price))]

    ui(rec_info)

    return rec_info


def show_hall(sel_hall, hall, sel_time):
    """
    좌석 정보를 print 합니다.
    :param sel_hall: 선택한 상영관 정보 list (세로열, 가로줄)
    :param hall: 선택한 상영관 str
    :param sel_time: 선택한 시간대 int (HHMM 꼴)
    :return: 예약된 좌석 정보를 담은 2차원 list is_occupied
    """
    line = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    hall_2D = []
    for i in range(sel_hall[0]):
        hall_2D.append(['.' for i in range(sel_hall[1])])

    is_occupied = []

    occupy_file = open('hall_{}{}.txt'.format(hall, sel_time), 'r')
    occupy_line = occupy_file.read()
    # print(occupy_line)
    # # 테스트전용

    occupy_element = occupy_line.split('\n')

    # element 의 형식 -> ['2,3', '1,10'...''] 꼴

    [is_occupied.append(i.split(',')) for i in occupy_element]
    del is_occupied[-1]
    # is_occupied 의 형식 -> [['2','3'],['1','10']] 꼴

    # print(is_occupied)
    # # 테스트전용
    if len(is_occupied) > 0:
        if is_occupied[-1] == ['']:
            is_occupied.remove([''])
        for n in range(len(is_occupied)):
            hall_2D[int(is_occupied[n][0])][int(is_occupied[n][1]) - 1] = '#'
        # 좌석번호의 경우 저장할 때 +1 해주었기 때문에 다시 빼줍니다.

    print('    ', end='')
    for x in range(sel_hall[1]):
        print(f'{x + 1:^3}', end='')
    print('')
    for y in range(len(hall_2D)):
        print(f'{line[y]:<4}', end='')
        # 좌측 열 알파벳 표시
        for x in range(len(hall_2D[y])):
            print(f'{hall_2D[y][x]:^3}', end='')
            # 빈칸, 예약칸 표시
        print('')
    print('')
    # 002분반 실습 week3 fstring 으로 문자열 정렬하기
    return is_occupied
