board = [[5,3,0,0,7,0,0,0,0],\
         [6,0,0,1,9,5,0,0,0],\
         [0,9,8,0,0,0,0,6,0],\
         [8,0,0,0,6,0,0,0,3],\
         [4,0,0,8,0,3,0,0,1],\
         [7,0,0,0,2,0,0,0,6],\
         [0,6,0,0,0,0,2,8,0],\
         [0,0,0,4,1,9,0,0,5],\
         [0,0,0,0,8,0,0,7,9]]

def print_board():
    global board
    for y in range(9):
        for x in range(9):
            print(' ',end='')
            if x in [2,5]:
                print(board[y][x], end=' |')
            else:
                print(board[y][x], end=' ')
        if y in [2,5]:
            print('\n---------|---------|--------')
        else:
            print()

# 動作確認
print('盤面の印刷')
print_board()

def possible(y,x,n):
    global board
    for i in range(0,9):
        if board[y][i] == n:
            return False
    for i in range(0,9):
        if board[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if board[y0+i][x0+j] == n:
                return False
    return True

# 動作確認
print( '\n4行4列に4は置けるか？', possible(4,4,4) )
print( '4行4列に5は置けるか？', possible(4,4,5) )

def solve():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0
                return
    print_board()

# 動作確認
print('\n解はどうなるかな？')
solve()

