import os

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

#skeleton of board using dictionaries

def printboard(boardx):
    print(boardx['7']+' | '+boardx['8']+' | '+boardx['9'])
    print('--+---+--')
    print(boardx['4']+' | '+boardx['5']+' | '+boardx['6'])
    print('--+---+--')
    print(boardx['1']+' | '+boardx['2']+' | '+boardx['3'])

#print function to show board

def tictactoe():

    move = 'X'
    count = 0

    for i in range(20):
        print()
        printboard(board)
        print()
        intake = input()

        if board[intake]==' ':
            board[intake]=move
            count+=1
        else:
            continue

        #alternating moves

        if move=='X':
            move='O'
        else:
            move='X'

        #winning condition defined
        if count >= 5:

            if board['7']==board['8']==board['9'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break
            elif board['4']==board['5']==board['6'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break
            elif board['1']==board['2']==board['3'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break
            elif board['7']==board['4']==board['1'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break
            elif board['8']==board['5']==board['2'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break
            elif board['9']==board['6']==board['3'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break
            elif board['7']==board['5']==board['3'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break
            elif board['1']==board['5']==board['9'] != ' ':
                printboard(board)
                print('\nwin! win!')
                break

        if count == 9:
            print()
            printboard(board)
            print('\ntie!')
            break
            
tictactoe()

res=input("\nplay again ? (y/n): ")
if res == 'y':
    os.system('python3 tictactoe.py')
