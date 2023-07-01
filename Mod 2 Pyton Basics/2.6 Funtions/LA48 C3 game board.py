import random

board = [' '] * 9

def set_random(board,computer_mark):
    board[random.randint(0, 8)] = computer_mark

def print_board(board):
    lines = [' +--%s--+' % ('-'*5).join(['A','B','C'])]
    for i in range(3):
        lines.append('%d|  %s  |' % (i,'  |  '.join(board[3*i:(3*i+3)])))
        if i < 2:
            lines.append(' ' + '-'*19)
    lines.append(' +%s+' % ('-'*17))
    print('\n |     |     |     |\n'.join(lines))

print_board(board)

random.seed(0)
set_random(board,'X')

print_board(board)
