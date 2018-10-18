import random
import argparse

class Board:
    def __init__(self):
        self.squares = [' '] * 9 

    def playermove(self, n):
        if self.validsquare(n):
            self.squares[n] = 'X'
            return True        
        return False

    def validsquare(self, n):
        if self.squares[n] != ' ':
            return False
        return True

    def randommove(self):
        possiblemove = []
        for i in range(9):
            if self.squares[i] == ' ':
                possiblemove.append(i)
        if possiblemove != []:
            return random.choice(possiblemove)
    
    def smartmove(self, mark):
        for i in range(9):
            if self.squares[i] == ' ':
                self.squares[i] = mark
                if self.win()[0] == True:
                    self.squares[i] = ' '
                    return i
                self.squares[i] = ' '
        return -1

    def computermove(self):
        move1 = self.smartmove('O')
        move2 = self.smartmove('X')
        move = -1
        if move1 != -1:
            move = move1
        elif move2 != -1:
            move = move2
        else:
            n = self.randommove()
            if self.validsquare(n):
                move = n
        self.squares[move] = 'O'  

    def check_row(self, n):
        squares = self.squares
        if squares[3 * n] != ' ':
            for i in range(1,3):
                if squares[3 * n + i] != squares[3 * n]:
                    return False, ' '
            return True, squares[n * 3]
        return False, ' '

    def check_column(self, n):
        squares = self.squares
        if squares[n] != ' ':
            for i in range(1, 3):
                if squares[n + 3 * i] != squares[n]:
                    return False, ' '
            return True, squares[n]
        return False, ' '


    def win(self):
        squares = self.squares
        for i in range(3):
            over, winner = self.check_row(i)
            if over:
                return over, winner
            over, winner = self.check_column(i)
            if over:
                return over, winner        
        if squares[0] != ' ' and squares[4] == squares[0] and squares[0] == squares[8]:
            return True, squares[0]
        if squares[2] != ' ' and squares[2] == squares[4] and squares[4] == squares[6]:
            return True, squares[2]
        for i in range(9):
            if squares[i] == ' ':
                return False, ' '
        return True, ' '

    def drawboard(self):
        squares = self.squares
        print(squares[0] + '|' + squares[1] + '|' + squares[2])
        print(squares[3] + '|' + squares[4] + '|' + squares[5])  
        print(squares[6] + '|' + squares[7] + '|' + squares[8])
        print('------')
    
def game_loop(is_first):
    board = Board()
    board.drawboard()
    turn = is_first
    while True:
        if turn:
            entry = input('Please enter a number(from 1-9): ')
            entry = int(entry)
            if entry not in range(1,10):
                continue
            if not board.playermove(entry-1):
                continue
        else:
            board.computermove()
        board.drawboard()
        over, winner = board.win()
        if over:
            if winner == 'X' or winner == 'O':
                print(f'{winner} wins!')
            else:
                print('Tie')
            break
        turn = not turn

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--first', help = 'Do you want to play first? Y/N', default='Y')
    args = parser.parse_args()
    game_loop(args.first == 'Y')

if __name__ == '__main__':
    main()   