import random

# 첫번째로 선택한 곳의 숫자(a_choice)와 두번째로 선택한 곳의 숫자(b_choice) 변수를 만들고, 1P와 2P의 점수 변수를 만든다.

class cardgame:

    def __init__(self):
        self.board = [3, 2, 3, 4, 4, 5, 2, 7, 5, 7, 8, 8, 1, 1, 6, 6]
        self.turn = ""
        self.firstplayer_score = 0
        self.secondplayer_score = 0
        self.a_choice = 0
        self.b_choice = 0

    def turn_set(self):
        a = random.randrange(0, 2)
        if a == 0:
            self.turn = "1P"
        elif a == 1:
            self.turn = "2P"

# 첫번째는 랜덤 턴이기 때문에 랜덤으로 턴을 정하고, a의 값이 0이면 턴을 1P 또는 a의 값이 1이면 턴을 2P로 정한다.

    def turn_change(self):
        if self.turn == "1P":
            self.turn = "2P"
        elif self.turn == "2P":
            self.turn = "1P"

# 전 턴이 1P라면 턴을 2P로 바꾼다. 전 턴이 2P라면 턴을 1P로 바꾼다.

    def check_board(self):
        for i in range(0, len(self.board)):
            if self.board[i] != "*":
                check = check + 1
                if check == 16:
                    print("game finished")
                    if self.firstplayer_score > self.secondplayer_score:
                        print(self.firstplayer_score)
                        print("1P Win")
                    elif self.secondplayer_score > self.firstplayer_score:
                        print(self.secondplayer_score)
                        print("2P Win")
                    elif self.firstplayer_score == self.secondplayer_score:
                        print(self.firstplayer_score, self.secondplayer_score)
                        print("1P, 2P Tie")

# 판 리스트의 항목이 공백인지 확인하고, 공백이 아니면 1을 더한다. 만일 확인 변수의 합이 16이라면, 게임을 끝내고 누가 이겼는지 점수를 비교하여 승부를 가린다.

    def add_score(self):
        if self.a_choice == self.b_choice:
            if self.turn == "1P":
                self.firstplayer_score = self.firstplayer_score + 1
            elif self.turn == "2P":
                self.secondplayer_score = self.secondplayer_score + 1

# 누구의 차례인지 알기 위해서 턴 변수를 불러온다. 첫번째 선택한 카드와 두번째 선택한 카드의 값이 서로 같으면 턴이 1P인지 2P인지 비교한다.
# 만일 턴이 1P라면, 1P의 점수를 더한다. 만일 턴이 2P라면, 2P의 점수를 더한다. 점수는 리턴한다.

player = cardgame()