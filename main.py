# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import tkinter as tk
from tkinter import font as tkFont
from tkinter import Label
from tkinter import *
class Square:
    def __init__(self, color, word,blockNumber):
        self.word = word
        self.color = color
        self.blockNumber = blockNumber
        self.state = False
        self.bomb = False

    def get_word(self):
        return self.word

    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color
		
    def change_state(self):
        self.state = not state

    def getBlockNumber(self):
        return self.blockNumber


    def setasbomb(self):
        self.color = 'White'
        self.bomb = True


class Game:
    def __init__(self):
        self.squares = []
        self.red = 0
        self.redMax = 9
        self.blueMax = 8
        self.blue = 0
        self.redFirst = False
        self.selectedWord = []
        self.filledBlock = []
        self.redSquares = []
        self.blueSquares = []
        self.specialWords = 5

    def determineFirst(self):
        num = random.randint(0,1)
        if num == 1:
            self.redFirst = True
        else:
            self.redMax = 8
            self.blueMax = 9

    def selectSpecialWord(self):
        f = open('personal')
        lines = f.readlines()
        if not lines:
            return False
        while True:
            ranv = random.randint(0,4)
            if lines[ranv].strip('\n') not in self.selectedWord:
                word = lines[ranv].strip('\n')
                self.selectedWord.append(word)
                return word.upper()
            else:
                return False

    def selectRandomWord(self):
        f = open('words')
        lines = f.readlines()
        while True:
            ranv = random.randint(0,672)
            if lines[ranv].strip('\n') not in self.selectedWord:
                word = lines[ranv].strip('\n')
                self.selectedWord.append(word)
                return word.upper()


    def neuturalSquares(self):
        for i in range(0,25):
            ranv = random.randint(1,10)
            if(ranv % 2 == 0):
                testWord = self.selectSpecialWord()
                word = testWord if testWord else self.selectRandomWord()
            else:
                word = self.selectRandomWord()
            #word = "fed"
            sq = Square('grey',word,i)
            self.squares.append(sq)

    def setBomb(self):
        while True:
            randV = random.randint(0,24)
            if randV not in self.redSquares and randV not in self.blueSquares:
                self.squares[randV].setasbomb()
                break


    def setAllSquares(self):
        self.determineFirst()
        self.neuturalSquares()
        while True:
            randv = random.randint(0,24)
            if self.red == self.redMax:
                break
            if randv not in self.redSquares and randv not in self.blueSquares:
                self.redSquares.append(randv)
                self.squares[randv].set_color('red')
                self.red += 1
        while True:
            randv = random.randint(0, 24)
            if self.blue == self.blueMax:
                break
            if randv not in self.redSquares and randv not in self.blueSquares:
                self.blueSquares.append(randv)
                self.squares[randv].set_color('blue')
                self.blue += 1
        self.setBomb()

    def printBoard(self):
        self.setAllSquares()
        counter = 0
        for i in range(0,5):
            for j in range(0,5):
                print(self.squares[counter].word,end='  ')
                counter += 1
            print("")

    def printColors(self):
        counter = 0
        for i in range(0,5):
            for j in range(0,5):
                print(self.squares[counter].color,end='  ')
                counter += 1
            print("")
class GUI:
    def __init__(self):
        game = Game()
        game.printBoard()
        game.printColors()
        self.redTurn = game.redFirst
        self.color = 'red'
        if not self.redTurn:
            self.color = 'blue'
        self.redScore = game.redMax
        self.blueScore = game.blueMax
        self.GameMaster(game)
        self.master = tk.Tk()
        self.master.configure(bg='black')
        self.master.title("CODE NAMES")
        self.buttons = {}
        self.allWords = {}
        self.pressedWords = []
        helv36 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
        helv5 = tkFont.Font(family='Helvetica', size=5, weight=tkFont.BOLD)
        self.endTurn = tk.Checkbutton(self.master, indicatoron=0, activebackground='black',
                                                           background="white",
                                                           selectcolor='white',
                                                           text='END TURN', foreground="black",
                                                           width=15, height=5, font=helv36,command=self.endTurn)
        self.endTurn.grid(row=10, column=9)

        label = Label(self.master, text=str(self.redScore)+'-'+str(self.blueScore),font=helv5,fg=self.color,bg='black')
        label.grid(row=0, column=3)
        counter = 0
        for i in range(5,10):
            for j in range(0,5):
                self.allWords[counter] = game.squares[counter].word
                if game.squares[counter].color == 'red':
                    self.buttons[counter] = tk.Checkbutton(self.master, indicatoron=0, activebackground='black',
                                                           background="green",
                                                           selectcolor=game.squares[counter].color,
                                                           text=game.squares[counter].word, foreground="black",
                                                           width=15, height=5, font=helv36, command=lambda text=game.squares[counter].word: self.adjustRed(text))
                elif game.squares[counter].color == 'blue':
                    self.buttons[counter] = tk.Checkbutton(self.master, indicatoron=0, activebackground='black',
                                                           background="green",
                                                           selectcolor=game.squares[counter].color,
                                                           text=game.squares[counter].word, foreground="black",
                                                           width=15, height=5, font=helv36, command=lambda text=game.squares[counter].word: self.adjustBlue(text))
                elif game.squares[counter].color == 'White':
                    self.buttons[counter] = tk.Checkbutton(self.master, indicatoron=0, activebackground='black',
                                                           background="green",
                                                           selectcolor=game.squares[counter].color,
                                                           text=game.squares[counter].word, foreground="black",
                                                           width=15, height=5, font=helv36,command=self.bombPressed)
                else:
                    self.buttons[counter] = tk.Checkbutton(self.master, indicatoron=0, activebackground='black', background="green",
                                                       selectcolor=game.squares[counter].color,text=game.squares[counter].word, foreground="black",
                                                       width=15, height=5, font=helv36)
                self.buttons[counter].grid(row=(i+1), column=(j+1))
                counter += 1
        self.master.mainloop()

    def bombPressed(self):
        self.master.destroy()

    def adjustRed(self,word):
        if word not in self.pressedWords:
            self.redScore -= 1
            self.pressedWords.append(word)
        else:
            self.redScore += 1
            self.pressedWords.remove(word)
        helv5 = tkFont.Font(family='Helvetica', size=5, weight=tkFont.BOLD)
        label = Label(self.master, text=str(self.redScore)+'-'+str(self.blueScore),font=helv5,fg=self.color,bg='black')
        label.grid(row=0, column=3)

    def adjustBlue(self,word):
        if word not in self.pressedWords:
            self.blueScore -= 1
            self.pressedWords.append(word)
        else:
            self.blueScore += 1
            self.pressedWords.remove(word)
        helv5 = tkFont.Font(family='Helvetica', size=5, weight=tkFont.BOLD)
        label = Label(self.master, text=str(self.redScore)+'-'+str(self.blueScore),font=helv5,fg=self.color,bg='black')
        label.grid(row=0, column=3)

    def endTurn(self):
        self.redTurn = not self.redTurn
        if not self.redTurn:
            self.color = 'blue'
        else:
            self.color = 'red'
        helv5 = tkFont.Font(family='Helvetica', size=5, weight=tkFont.BOLD)
        label = Label(self.master, text=str(self.redScore)+'-'+str(self.blueScore),font=helv5,fg=self.color,bg='black')
        label.grid(row=0, column=3)



    def GameMaster(self,game):
        self.master = tk.Tk()
        self.master.title("Game Masters ONLY")
        helv36 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)
        # self.master.geometry("2x1")
        self.buttons = {}
        counter = 0
        for i in range(5, 10):
            for j in range(0, 5):
                self.buttons[counter] = tk.Checkbutton(self.master, indicatoron=0, activebackground='black',
                                                       background=game.squares[counter].color,
                                                       selectcolor=game.squares[counter].color,
                                                       text=game.squares[counter].word, foreground="black",
                                                       width=15, height=5, font=helv36)
                self.buttons[counter].grid(row=(i + 1), column=(j + 1))
                counter += 1
        #self.master.mainloop()


# Press the green self.button in the gutter to run the script.
if __name__ == '__main__':
    # g = Game()
    # g.printBoard()
    # g.printColors()
    h = GUI()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
