import random

su = 90  # 초기 강화 확률
plus = 2  # 강화 확률 증가 상수
tn = 1  # 시도 횟수
sun = 0  # 강화 시뮬레이터 상수(성공확률)
rf = [0 for i in range(100)]  # 강화 시뮬레이터 상수
rn = 0  # 현재 강화
max_R = 7  # 최대 강화


def rain_force():
    global su
    global rn
    su = 90
    if rn == max_R:  # 최대 강화 수에 도달 시
        print(max_R, '최대 강화 단계에 도달했습니다')
        exit(0)
    for z in range(1, rn + 1):
        if z < 5:
            su -= 15
        elif 5 <= z < 6:
            su = 10
        elif z == 6:
            su = 1


def m_menu():
    global su
    global rn
    rn = int(input('현재 강화되어있는 강 수를 입력하세요(0-7):'))
    if rn == max_R:  # 최대 강화 수에 도달 시
        print(max_R, '강은 강화가 불가능합니다.')
        exit(0)
    elif 0 <= rn < max_R:  # 강화가 가능한 수치일 때, 해당 강화 정도의 확률을 맞춘다
        rain_force()
    else:
        print("잘못된 값을 입력했습니다.")
        m_menu()


def r_menuS1():
    a = input('이어서 도전 하시겠습니까? y/n:')
    if a == 'y':
        global tn
        global sun
        global su
        tn = 1
        rain_force()
        sun = su
        f = 1
        return f
    elif a == 'n':
        f = 0
        return f
    else:
        print('잘못된 값을 입력하셨습니다.')
        r_menuS1()


def r_menuS2():
    a = input('이어서 도전 하시겠습니까? y/n:')
    if a == 'y':
        global tn
        global su
        global plus
        global rf
        global sun
        tn = 1
        rain_force()
        sun = su
        rf = [0 for i in range(100)]
        while sun != 0:
            ran = random.randrange(0, 100)
            if rf[ran] == 0:
                rf[ran] = 1
                sun -= 1
        f = 1
        return f
    elif a == 'n':
        f = 0
        return f
    else:
        print('잘못된 값을 입력하셨습니다.')
        r_menuS2()


def r_menuF1():
    a = input('재도전 하시겠습니까? y/n:')
    if a == 'y':
        global tn
        global su
        global sun
        tn += 1
        if rn < 5:
            if su + 2 > 100:
                su = 100
            else:
                su += 2
            sun += su * 10
        f = 1
        return f
    elif a == 'n':
        f = 0
        return f
    else:
        print('잘못된 값을 입력하셨습니다.')
        r_menuF1()


def r_menuF2():
    a = input('재도전 하시겠습니까? y/n:')
    if a == 'y':
        global tn
        global su
        global plus
        global rf
        tn += 1
        if rn < 5:
            if su + 2 > 100:
                su = 100
            else:
                su += 2
            while plus != 0:
                ran = random.randrange(0, 100)
                if rf[ran] == 0:
                    rf[ran] = 1
                    plus -= 1
        f = 1
        return f
    elif a == 'n':
        f = 0
        return f
    else:
        print('잘못된 값을 입력하셨습니다.')
        r_menuF2()


def f_menu():
    global sun
    global br
    global rn
    global tn
    global rf
    sun = su
    qu = int(input('강화 시스템 형태를 입력해주세요. 1, 2: '))
    if qu == 1:
        while br == 1:
            print('%d번째 시도, 현재 %d강 성공 확률은 %r%%입니다.' % (tn, rn, su))
            ran = random.randrange(0, 100)
            if ran < sun:
                print('성공')
                rn += 1
                br = r_menuS1()
            else:
                print('실패')
                if rn < 5:
                    print('강화확률이 2%% 상승했습니다.')
                br = r_menuF1()

    elif qu == 2:
        while sun != 0:
            ran = random.randrange(0, 100)
            if rf[ran] == 0:
                rf[ran] = 1
                sun -= 1
        while br == 1:
            print('%d번째 시도, 현재 %d강 성공 확률은 %r%%입니다.' % (tn, rn, su))
            res = rf[random.randrange(0, 100)]
            if res == 0:
                print('실패')
                if rn < 5:
                    print('강화확률이 2%% 상승했습니다.')
                br = r_menuF2()
            elif res == 1:
                print('성공')
                rn += 1
                br = r_menuS2()
            else:
                print(res)
                print('오류발생')

    else:
        print('잘못된 값을 입력하셨습니다.')
        f_menu()


br = 1
m_menu()
f_menu()

