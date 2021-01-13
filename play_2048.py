from tkinter import *
from backend_2048 import *

root = Tk()

board = Board()

colors = {
	0 : "#ffffff",
	2 : "#eee4da",
	4 : "#ebd3a7",
	8 : "#f2b179",
	16 : "#f59563",
	32 : "#f67c5f",
	64 : "#f65e3b",
	128 : "#edcf72",
	256 : "#edcc61",
	512 : "#edc850",
	1024 : "#edc53f",
	2048 : "#edc22e"
}

gameWonLabel = Label(root, 
						text = "You Won :)", 
						bg = "green", justify = CENTER, 
						width=10, height=3, font=("Verdana", 10, "bold"))

gameLostLabel = Label(root, 
						text = "You Lost :(", 
						bg = "red", justify = CENTER, 
						width=10, height=3, font=("Verdana", 10, "bold"))

def display():
	boardLabels = []
	for i in range(4):
		rowLabelList = []
		for j in range(4):
			if board.boardState[i][j] == 0:
				labeltext = ""
			else:
				labeltext = str(board.boardState[i][j])

			label = Label(root, text = labeltext, 
							bg = colors[board.boardState[i][j]], 
							justify = CENTER, 
							width=5, height=2, 
							font=("Verdana", 40, "bold"))
			rowLabelList.append(label)
		boardLabels.append(rowLabelList)

	for i in range(4):
		for j in range(4):
			boardLabels[i][j].grid(row = i, column = j, padx=2, pady=2)

	score = Label(root, text = "Score\n" + str(board.getMax()),  
							justify = CENTER, 
							width=5, height=2, 
							font=("Verdana", 30, "bold"))
	score.grid(row = 0, column = 4)


def displayGameWon():
	global gameWonLabel
	gameWonLabel.grid(row = 1, column = 4)


def displayGameLost():
	global gameLostLabel
	gameLostLabel.grid(row = 1, column = 4)


def leftkey(event):
	board.moveLeft()
	display()
	if board.gameWon == True:
		displayGameWon()
	elif board.gameLost == True:
		displayGameLost()
def rightkey(event):
	board.moveRight()
	display()
	if board.gameWon == True:
		displayGameWon()
	elif board.gameLost == True:
		displayGameLost()
def upkey(event):
	board.moveUp()
	display()
	if board.gameWon == True:
		displayGameWon()
	elif board.gameLost == True:
		displayGameLost()
def downkey(event):
	board.moveDown()
	display()
	if board.gameWon == True:
		displayGameWon()
	elif board.gameLost == True:
		displayGameLost()
def gamereset():
	global board
	global gameLostLabel
	global gameWonLabel
	gameLostLabel.grid_forget()
	gameWonLabel.grid_forget()
	board = Board()
	display()


reset = Button(root, text="New Game", height=3, width=8, 
					bd=4, bg="red", fg="white", 
					font=("Verdana", 10, "bold"), command = gamereset)
reset.grid(row = 2, column = 4)


display()
root.title("2048")
root.bind('<Left>', leftkey)
root.bind('<Right>', rightkey)
root.bind('<Up>', upkey)
root.bind('<Down>', downkey)

root.mainloop()