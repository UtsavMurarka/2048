import random

class Board:

	boardState = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	gameWon = False
	gameLost = False
	# Constructor for Board Class
	# Initializes the board with 2 tiles each of value 2, placed anywhere randomly
	def __init__(self):
		self.boardState = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
		initialNonEmptyRow1 = random.randint(0, 3)
		initialNonEmptyCol1 = random.randint(0, 3)
		initialNonEmptyRow2 = random.randint(0, 3)
		initialNonEmptyCol2 = random.randint(0, 3)
		while ( (initialNonEmptyRow1==initialNonEmptyRow2) and (initialNonEmptyCol1==initialNonEmptyCol2)):
			initialNonEmptyRow2 = random.randint(0, 3)
			initialNonEmptyCol2 = random.randint(0, 3)

		tileToInsert = [2, 4]
		tileProbability = [0.5, 0.5]

		selectTile = random.choices(tileToInsert, tileProbability)
		self.boardState[initialNonEmptyRow1][initialNonEmptyCol1] = selectTile[0]
		
		selectTile = random.choices(tileToInsert, tileProbability)
		self.boardState[initialNonEmptyRow2][initialNonEmptyCol2] = selectTile[0]


	def moveLeft(self):
		# Logic for left move
		if not (self.gameLost or self.gameWon):
			for i in range(len(self.boardState)):
				self._shiftAndMergeRow(i, "Left")
			
			# insert random tile
			self._insertRandomTile()
			if self.checkGameLost() == True:
				self.gameLost = True

	def moveRight(self):
		# Logic for right move
		if not (self.gameLost or self.gameWon):
			for i in range(len(self.boardState)):
				self._shiftAndMergeRow(i, "Right")
			
			# insert random tile
			self._insertRandomTile()
			if self.checkGameLost() == True:
				self.gameLost = True

	def moveUp(self):
		# Logic for Up move
		if not (self.gameLost or self.gameWon):
			for i in range(len(self.boardState)):
				self._shiftAndMergeCol(i, "Up")
			
			# insert random tile
			self._insertRandomTile()
			if self.checkGameLost() == True:
				self.gameLost = True
	
	def moveDown(self):
		# Logic for Down move
		if not (self.gameLost or self.gameWon):
			for i in range(len(self.boardState)):
				self._shiftAndMergeCol(i, "Down")
			
			# insert random tile
			self._insertRandomTile()
			if self.checkGameLost() == True:
				self.gameLost = True


	def _insertRandomTile(self):		
		# insert a tile of value 2 or 4 with probability ratio 8:2
		tileToInsert = [2, 4]
		tileProbability = [0.8, 0.2]
		selectTile = random.choices(tileToInsert, tileProbability)
		self._insertAtRandomPosition(selectTile[0])

	def _insertAtRandomPosition(self, tileValue):
		# make a list of empty positions on board
		emptyList = []
		for i in range(len(self.boardState)):
			for j in range((len(self.boardState))):
				if self.boardState[i][j] == 0:
					emptyList.append([i, j])

		if len(emptyList) > 0:
			# select a position at random
			insertTileAt = random.randint(0, len(emptyList) - 1)
			# insert
			self.boardState[emptyList[insertTileAt][0]][emptyList[insertTileAt][1]] = tileValue


	def getMax(self):
		maxVal = 0
		for i in range(len(self.boardState)):
			for j in range((len(self.boardState))):
				if self.boardState[i][j] > maxVal:
					maxVal = self.boardState[i][j]
		return maxVal

	def checkGameLost(self):
		for row in self.boardState:
			for val in row:
				if val == 0:
					return False

		for i in range(len(self.boardState)):
			for j in range(len(self.boardState) - 1):
				if self.boardState[i][j] == self.boardState[i][j+1]:
					return False

		for i in range(len(self.boardState)):
			for j in range(len(self.boardState) - 1):
				if self.boardState[j][i] == self.boardState[j+1][i]:
					return False

		return True

	def _shiftAndMergeRow(self, row, direction):
		# direction can be left or right depending on the move by the player
		if direction == "Left":
			# Shift every tile to left if possible
			for i in range(len(self.boardState)):
				for j in range(1, len(self.boardState)):
					if self.boardState[row][j-1] == 0:
						self.boardState[row][j-1] = self.boardState[row][j]
						self.boardState[row][j] = 0

			# Merge Equal Tiles
			for i in range(len(self.boardState) - 1):
				if self.boardState[row][i] == self.boardState[row][i+1]:
					self.boardState[row][i] *= 2
					self.boardState[row][i + 1] = 0
					if self.boardState[row][i] == 2048:
						self.gameWon = True

			# Left Shift again to fill gaps created by merging
			for i in range(len(self.boardState)):
				for j in range(1, len(self.boardState)):
					if self.boardState[row][j-1] == 0:
						self.boardState[row][j-1] = self.boardState[row][j]
						self.boardState[row][j] = 0


		if direction == "Right":
			# Shift every tile to right if possible
			for i in range(len(self.boardState)):
				for j in range(0, len(self.boardState)-1):
					if self.boardState[row][j+1] == 0:
						self.boardState[row][j+1] = self.boardState[row][j]
						self.boardState[row][j] = 0

			# Merge Equal Tiles
			for i in range(len(self.boardState) - 1, 0, -1):
				if self.boardState[row][i] == self.boardState[row][i-1]:
					self.boardState[row][i] *= 2
					self.boardState[row][i - 1] = 0
					if self.boardState[row][i] == 2048:
						self.gameWon = True

			# Right Shift again to fill gaps created by merging
			for i in range(len(self.boardState)):
				for j in range(0, len(self.boardState)-1):
					if self.boardState[row][j+1] == 0:
						self.boardState[row][j+1] = self.boardState[row][j]
						self.boardState[row][j] = 0


	def _shiftAndMergeCol(self, col, direction):
		# direction can be Up or Down depending on the move by the player
		if direction == "Up":
			# Shift every tile to Up if possible
			for i in range(len(self.boardState)):
				for j in range(1, len(self.boardState)):
					if self.boardState[j-1][col] == 0:
						self.boardState[j-1][col] = self.boardState[j][col]
						self.boardState[j][col] = 0

			# Merge Equal Tiles
			for i in range(len(self.boardState) - 1):
				if self.boardState[i][col] == self.boardState[i+1][col]:
					self.boardState[i][col] *= 2
					self.boardState[i+1][col] = 0
					if self.boardState[i][col] == 2048:
						self.gameWon = True

			# Up Shift again to fill gaps created by merging
			for i in range(len(self.boardState)):
				for j in range(1, len(self.boardState)):
					if self.boardState[j-1][col] == 0:
						self.boardState[j-1][col] = self.boardState[j][col]
						self.boardState[j][col] = 0


		if direction == "Down":
			# Shift every tile to Down if possible
			for i in range(len(self.boardState)):
				for j in range(0, len(self.boardState)-1):
					if self.boardState[j+1][col] == 0:
						self.boardState[j+1][col] = self.boardState[j][col]
						self.boardState[j][col] = 0

			# Merge Equal Tiles
			for i in range(len(self.boardState) - 1, 0, -1):
				if self.boardState[i][col] == self.boardState[i-1][col]:
					self.boardState[i][col] *= 2
					self.boardState[i-1][col] = 0
					if self.boardState[i][col] == 2048:
						self.gameWon = True

			# Down Shift again to fill gaps created by merging
			for i in range(len(self.boardState)):
				for j in range(0, len(self.boardState)-1):
					if self.boardState[j+1][col] == 0:
						self.boardState[j+1][col] = self.boardState[j][col]
						self.boardState[j][col] = 0
