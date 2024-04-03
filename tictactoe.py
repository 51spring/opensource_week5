# 보드 초기화
# 플레이어 설정 ( 사용자가 X, 컴퓨터가 O)
## 반복 ##
# 게임 보드를 출력
# 플레이어의 입력 받기
# 입력이 유효한지 확인. 유효하지 않으면 다시 입력
# 입력 위치에 현재 플레이어를 표시
# 게임이 끝났는지 확인

import random

# 게임 보드 초기화
board = [[' ' for _ in range(3)] for _ in range(3)]

# 플레이어 설정
player = 'X'
computer = 'O'

# 게임 보드 출력 함수
def print_board(board):
    for row in board:
        print(row)
    print()

# 입력 위치 확인 함수
def valid_move(x, y):
    return board[x][y] == ' '

# 게임 종료 확인 함수
def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# 게임 진행
while True:
    print_board(board)
    x = input("x좌표를 입력하세요: ")
    y = input("y좌표를 입력하세요: ")
    x = int(x)
    y = int(y)
    if valid_move(x, y):
        board[x][y] = player
        if check_win(board, player):
            print_board(board)
            print("이겼어요!")
            break
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")
    print_board(board)
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    if valid_move(x, y):
        board[x][y] = computer
        if check_win(board, computer):
            print_board(board)
            print("졌어요")
            break