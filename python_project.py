import time, sys, random


class Player:
    def __init__(self, name):
        self.name = name
        self.ATT = random.randint(50, 100)
        self.PAS = random.randint(50, 100)
        self.DEF = random.randint(50, 100)
        self.STA = random.randint(1, 100)

    def see_parameter(self):
        print("{0:>3}".format(self.name), "{0:>4}".format(self.ATT), "{0:>4}".format(self.PAS),
              "{0:>4}".format(self.DEF), "{0:>4}".format(self.STA))

    def __str__(self):
        print("{0:>3}".format(self.name), "{0:>3}".format(self.ATT), "{0:>4}".format(self.PAS),
              "{0:>4}".format(self.DEF), "{0:>4}".format(self.STA))


    def nurf(self):
        self.ATT = (0.5 + 0.005 * self.STA) * self.ATT
        self.PAS = (0.5 + 0.005 * self.STA) * self.PAS
        self.DEF = (0.5 + 0.005 * self.STA) * self.DEF


class PlayersAct:
    def __init__(self, players, ball, score1, score2):
        self.players3 = players
        self.ball = ball
        self.score1 = score1
        self.score2 = score2
        self.pass_succ = [0, 0, 0, 0]
        self.goal_succ = [0, 0, 0, 0]
        self.possession_rate = [0, 0]
        self.football()
        self.summaries()

    def whereisball(self):
        if self.ball == 0:
            print("  ⓞ■  □■")
            print("■         □")
            print("  □■  □■")
        elif self.ball == 1:
            print("  □ⓞ  □■")
            print("■         □")
            print("  □■  □■")
        elif self.ball == 2:
            print("  □■  ⓞ■")
            print("■         □")
            print("  □■  □■")
        elif self.ball == 3:
            print("  □■  □ⓞ")
            print("■         □")
            print("  □■  □■")
        elif self.ball == 4:
            print("  □■  □■")
            print("ⓞ         □")
            print("  □■  □■")
        elif self.ball == 5:
            print("  □■  □■")
            print("■         ⓞ")
            print("  □■  □■")
        elif self.ball == 6:
            print("  □■  □■")
            print("■         □")
            print("  ⓞ■  □■")
        elif self.ball == 7:
            print("  □■  □■")
            print("■         □")
            print("  □ⓞ  □■")
        elif self.ball == 8:
            print("  □■  □■")
            print("■         □")
            print("  □■  ⓞ■")
        elif self.ball == 9:
            print("  □■  □■")
            print("■         □")
            print("  □■  □ⓞ")

    def summaries(self):
        print('=========================')
        print('      공 점유율  패스 성공률  슛 성공률')
        print('홈팀     %.2f' % (self.possession_rate[0] / sum(self.possession_rate) * 100),
              '     %.2f' % (self.pass_succ[0] / self.pass_succ[2] * 100),end='')
        if self.goal_succ[2] == 0:
            print('    %.2f' % 0)
        else:
            print('    %.2f' % (self.goal_succ[0] / self.goal_succ[2] * 100))
        print('원정팀   %.2f' % (self.possession_rate[1] / sum(self.possession_rate) * 100),
              '     %.2f' % (self.pass_succ[1] / self.pass_succ[3] * 100),end='')
        if self.goal_succ[3] == 0:
            print('    %.2f' % 0)
        else:
            print('    %.2f' % (self.goal_succ[1] / self.goal_succ[3] * 100))

    def passtowho(self, ball):
        i = random.randrange(0, 2)
        if (ball == 2 or ball == 8) and i == 0:
            return 0, 1
        elif (ball == 2 or ball == 8) and i == 1:
            return 6, 7
        elif (ball == 1 or ball == 7) and i == 0:
            return 3, 2
        elif (ball == 1 or ball == 7) and i == 1:
            return 9, 8
        elif ball == 4 and i == 0:
            return 1, 0
        elif ball == 4 and i == 1:
            return 7, 6
        elif ball == 5 and i == 0:
            return 2, 3
        elif ball == 5 and i == 1:
            return 8, 9
        else:
            print("오류로 종료합니다")
            exit()

    def whoisGK(self, ball):
        if ball == 0 or ball == 6:
            return 4
        elif ball == 3 or ball == 9:
            return 5
        else:
            print("오류로 종료합니다")
            exit()

    def passing(self, attacker):
        passer, defenser = self.passtowho(self.ball)
        pos = 50 + self.players3[attacker].PAS- self.players3[defenser].DEF
        i = random.randrange(0, 101)
        if i <= pos:
            print(self.players3[attacker].name + '이(가) 공을 ' + self.players3[passer].name + '에게 패스했습니다.')
            if attacker == 1 or attacker == 4 or attacker == 7:
                self.pass_succ[0] += 1
                self.pass_succ[2] += 1
                self.possession_rate[0] += 1
            elif attacker == 2 or attacker == 5 or attacker == 8:
                self.pass_succ[1] += 1
                self.pass_succ[3] += 1
                self.possession_rate[1] += 1
            return passer
        else:
            print(self.players3[attacker].name + '의 공을 ' + self.players3[defenser].name + '이(가) 뺏었습니다.')
            if attacker == 1 or attacker == 4 or attacker == 7:
                self.possession_rate[1] += 1
                self.pass_succ[2] += 1
            elif attacker == 2 or attacker == 5 or attacker == 8:
                self.possession_rate[0] += 1
                self.pass_succ[3] += 1
            return defenser

    def shoot(self, attacker):
        goalkeeper = self.whoisGK(self.ball)
        pos = 40 + int((self.players3[attacker].ATT - self.players3[goalkeeper].DEF) * 0.6)
        i = random.randrange(0, 101)
        if i <= pos:
            j = random.randrange(0, 2)
            if goalkeeper == 4:
                self.score2 += 1
                self.goal_succ[1] += 1
                self.goal_succ[3] += 1
                print('원정팀 ' + self.players3[attacker].name + '의골   홈', self.score1, ':', self.score2, '원정')
                if j == 0:
                    print(self.players3[1].name + '부터 다시 시작합니다')
                    return 1
                elif j == 1:
                    print(self.players3[7].name + '부터 다시 시작합니다')
                    return 7
            if goalkeeper == 5:
                self.score1 += 1
                self.goal_succ[0] += 1
                self.goal_succ[2] += 1
                print('홈팀 골   홈', self.score1, ':', self.score2, '원정')
                if j == 0:
                    print(self.players3[2].name + '부터 다시 시작합니다')
                    return 2
                elif j == 1:
                    print(self.players3[8].name + '부터 다시 시작합니다')
                    return 8
            else:
                print("뭔가 좆됬습니다 오류로 종료합니다")
                exit()
        else:
            print(self.players3[goalkeeper].name + '가 공을 막았습니다')
            if goalkeeper == 4:
                self.goal_succ[3] += 1
                self.possession_rate[0] += 1
            elif goalkeeper == 5:
                self.goal_succ[2] += 1
                self.possession_rate[1] += 1
            return goalkeeper

    def action(self, ball):
        if ball == 0 or ball == 3 or ball == 6 or ball == 9:
            return self.shoot(ball)
        else:
            return self.passing(ball)

    def football(self):
        turns = 10
        while turns >= 0:
            input()
            self.ball = self.action(self.ball)
            self.whereisball()
            print("=======================")
            turns -= 1
            # time.sleep(0.5)



class Game:
    def __init__(self):

        self.intro = Intro()
        self.team = Team()

        print("\n전반전")
        self.first_half = PlayersAct(self.team.players_in_game, 1,0,0)

        self.half_time()
        self.printline()

        print("후반전")
        self.second_half = PlayersAct(self.team.players_in_game, 2, self.first_half.score1, self.first_half.score2)

        self.final_summary()

    def final_summary(self):
        for i in range(4):
            sys.stdout.write("\r결과 산정중...." + str(3-i))
            sys.stdout.flush()
            time.sleep(1)
        print("\n==========최종 결과==========")
        print("           홈팀  원정팀")
        print("    골       %d"%self.second_half.score1 + "    %d"%self.second_half.score2)
        print(" 공 점유율  %.2f"%((self.first_half.possession_rate[0]+self.second_half.possession_rate[0])/(self.first_half.possession_rate[0]+self.first_half.possession_rate[1]+self.second_half.possession_rate[0]+self.second_half.possession_rate[1])*100)
              +" %.2f"%((self.first_half.possession_rate[1]+self.second_half.possession_rate[1])/(self.first_half.possession_rate[0]+self.first_half.possession_rate[1]+self.second_half.possession_rate[0]+self.second_half.possession_rate[1])*100))
        print("패스 성공률 %.2f"%((self.first_half.pass_succ[0]+self.second_half.pass_succ[0])/(self.first_half.pass_succ[2]+self.second_half.pass_succ[2])*100)
              +" %.2f"%((self.first_half.pass_succ[1]+self.second_half.pass_succ[1])/(self.first_half.pass_succ[3]+self.second_half.pass_succ[3])*100))
        print(" 슛 성공률  %.2f"%((self.first_half.goal_succ[0]+self.second_half.goal_succ[0])/(self.first_half.goal_succ[2]+self.second_half.goal_succ[2])*100)+
              " %.2f"%((self.first_half.goal_succ[1]+self.second_half.goal_succ[1])/(self.first_half.goal_succ[3]+self.second_half.goal_succ[3])*100))

    def half_time(self):
        for i in range(10):
            self.team.players_in_game[i].nurf()
        for i in range(11):
            sys.stdout.write("\r" + str(10-i) + "초 후에 후반전이 시작됩니다.")
            sys.stdout.flush()
            time.sleep(1)

    def printline(self):
        print('\n========================')


class Team:
    def __init__(self):
        self.playerlist = ['구민지', '김경일', '김단비', '김동훈', '김민정', '김상명', '김ㅤ송', '김종헌', '김형우', '류제범', '박종원', '변지영', '서석정',
                           '손상우', '송준영', '유호준', '이동언', '이소영', '이은혜', '이정우', '이지현', '이채림', '임낙현', '정지현', '정희택', '조준영',
                           '주현우', '채지혜', '하동호', '한혜림']
        self.players = []
        self.team = [[], []]
        self.players_in_game = [None, None, None, None, None, None, None, None, None, None]
        for i in range(30):
            self.players.append(Player(self.playerlist[i]))


        self.select_players()
        self.players_line_up()

    def location_home(self):
        print("  □②  □④")
        print("⑤          □")
        print("  □⑧  □⑩")
        a = []
        print("⑤골키퍼 : ",end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[4] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("②수비수 : ",end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[1] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("⑧수비수 : ",end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[7] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("④공격수 : ",end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[3] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("⑩공격수 : ",end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[9] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')

    def location_away(self):
        print("  ①□  ③□")
        print("□          ⑥")
        print("  ⑦□  ⑨□")
        a = []
        print("⑥골키퍼 : ", end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[5] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("③수비수 : ", end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[2] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("⑨수비수 : ", end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[8] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("①공격수 : ", end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[0] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')
        print("⑦공격수 : ", end='')
        while True:
            temp = input()
            if temp == '0' or temp == '1' or temp == '2' or temp == '3' or temp == '4':
                if temp not in a:
                    a.append(temp)
                    self.players_in_game[6] = self.team[0][int(temp)]
                    break
            print("다시 입력하세요 : ",end='')

    def select_team(self, i, n):
        self.team[i].append(self.players[n])
        del (self.players[n])

    def select_players(self):
        for j in range(5):
            for k in range(2):
                print("{0:^3}".format('번호'), "{0:^3}".format('이름'), "{0:^2}".format('슛'), "{0:^2}".format('패스'),
                      "{0:>2}".format('수비'), "{0:>4}".format('스태미너'))
                for i in range(len(self.players)):
                    print("{0:^3}".format(i), end='')
                    self.players[i].see_parameter()
                print("영입할 선수를 선택하세요 : ",end='')
                while True:
                    temp = input()
                    if temp in list(map(str, list(range(len(self.players))))):
                        self.select_team(k, int(temp))
                        break
                    print("다시 선택하세요 : ",end='')

        print("Home Team : ", end='')
        for i in range(len(self.team[0])):
            print(self.team[0][i].name, end=' ')
        print()
        print("Away Team : ", end='')
        for i in range(len(self.team[0])):
            print(self.team[1][i].name, end=' ')

        print()
        self.printline()

    def players_line_up(self):
        self.printline()
        print("홈팀 배치")
        print("번호  이름    슛  패스  수비 스테미너")
        for j in range(5):
            print("{0:^3}".format(j), end=' ')
            self.team[0][j].see_parameter()
        self.location_home()

        self.printline()
        print("원정팀 배치")
        print("번호 이름   슛  패스  수비 스테미너")
        for j in range(5):
            print(j, end=' ')
            self.team[1][j].see_parameter()
        self.location_away()

        home_list = [4, 1, 7, 3, 9]
        away_list = [5, 2, 8, 0, 6]

        print("===========\nHome Line-up")
        print("골키퍼   수비수   수비수   공격수   공격수 ")
        for i in home_list:
            print(self.players_in_game[i].name, ' ', end=' ')
        print()
        print("===========\nAway Line-up\n===========")
        print("골키퍼   수비수   수비수   공격수   공격수")
        for i in away_list:
            print(self.players_in_game[i].name, ' ', end=' ')

    def show_players(self):
        for i in range(len(self.players)):
            print(self.players[i].name)

    def printline(self):
        print('========================')


class Intro:
    def __init__(self):
        self.loading()
        self.title()

    def title(self):
        self.printline()
        print("  △▲△▲△")
        print("◀  풋  살  ▶")
        print("  ▽▼▽▼▽       ver.0.0.0.0.0.2 α...")
        input("Insert Coin")

    def loading(self):
        for self.i in range(51):
            self.a = ''
            self.b = str(int(self.i / 50 * 100))
            for self.j in range(self.i):
                self.a = self.a + "█"
            for self.j in range(50 - self.i):
                self.a = self.a + "░"
            sys.stdout.write("\r로딩중... " + self.a + self.b + "%")
            sys.stdout.flush()
            time.sleep(0.02)
        print('\n로딩 완료')

    def printline(self):
        print('========================')


a = Game()