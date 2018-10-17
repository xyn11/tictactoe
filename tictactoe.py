import random

class Board:
    def __init__(self):
        self.squares = [' '] * 9 
        self.movelist = []
        self.playeroccupy = set()
        self.computeroccupy = set()

    def playermove(self, n):
        if self.validsquare(n):
            self.squares[n] = 'X'
            self.movelist.append(n)
            self.playeroccupy.add(n) 
            return True        
        return False

    def validsquare(self, n):
        if n in self.movelist or n not in range(9):
            return False
        return True

    def randommove(self):
        possiblemove = []
        movelist = self.movelist
        for i in range(9):
            if i not in movelist:
                possiblemove.append(i)
        if possiblemove != []:
            return random.choice(possiblemove)


    def computermove(self):
        n = self.randommove()
        if self.validsquare(n):
            self.squares[n] = 'O'
            self.movelist.append(n)  
            self.computeroccupy.add(n)     

    def win(self):
        winset = [{0,1,2},{3,4,5},{6,7,8},{0,3,6},{1,4,7},{2,5,8},{0,4,8},{2,4,6}]
        for x in winset:
            if x == (x & self.playeroccupy):
                print('You win.')
            if x == (x & self.computeroccupy):
                print('You lose.')
        if len(self.movelist) == 9:
            print('Tie')

    def drawboard(self):
        squares = self.squares
        print(squares[0] + '|' + squares[1] + '|' + squares[2])
        print(squares[3] + '|' + squares[4] + '|' + squares[5])  
        print(squares[6] + '|' + squares[7] + '|' + squares[8])
        print('------')
    
game = Board()
game.drawboard()
random.seed(10)

while True:
    entry = input('Please enter a number(from 1-9): ')
    if game.playermove(int(entry)-1):        
        game.drawboard()
#        if game.win():
#            break
        game.computermove()
        game.drawboard()
#        if game.win():
#            break

