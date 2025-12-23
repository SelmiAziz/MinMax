from gameState import GameState

class TicTacToe(GameState):
	def __init__(self, board = None, player = 1):
		self.board = board if board is not None else ['.'] * 9
		self.player = player
	
	def getCurrentPlayer(self):
		return self.player
		
	def makeMove(self, move):
		new_board = list(self.board)
		print(move)
		if(self.player == 1): 
			new_board[move[0]*3+move[1]] = 'X'
		else:
			new_board[move[0]*3+move[1]] = 'O'
		return TicTacToe(new_board, -self.player)
	
	def evaluate(self):
		WIN_LINES = (
			(0,1,2), (3,4,5), (6,7,8),
			(0,3,6), (1,4,7), (2,5,8),
			(0,4,8), (2,4,6)
		)
		
		for a, b, c in WIN_LINES:
			if( self.board[a] == self.board[b] == self.board[c] ):
				if(self.board[a] == 'X'): return 1
				if(self.board[a] == 'O'): return -1
		if '.' in self.board : return None
		return 0
		
	
	def getMoves(self):
		l = []
		for i in range(len(self.board)):
			if(self.board[i] != 'X' and self.board[i] != 'O'):
				l.append((i//3, i%3))
		return l
	
	def display(self):
		for i in range(0,9,3):
			print(" ".join(self.board[i:i+3]))
		print("\n")
		
		
