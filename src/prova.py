from abc import ABC, abstractmethod


class GameState(ABC):
	@abstractmethod
	def getMoves(self): 
		pass
	@abstractmethod
	def getCurrentPlayer(self):
		pass
	@abstractmethod
	def evaluate(self):
		pass
	@abstractmethod
	def makeMove(self, move):
		pass


class TicTacToe(GameState):
	def __init__(self, board = None, player = 1):
		self.board = board if board else ['.']*9
		self.player = player
	
	def getCurrentPlayer(self):
		return self.player
	
	def makeMove(self, move):
		new_board = list(self.board)
		if(self.player == 1):
			new_board[move[0]*3+move[1]] = 'X'
		else:
			new_board[move[0]*3+move[1]] = 'O'
		return TicTacToe(new_board, -self.player)
	
	def evaluate(self):
		WIN_LINES = (
			(0,1,2),(3,4,5),(6,7,8),
			(0,3,6),(1,4,7),(2,5,8),
			(0,4,8),(2,4,6)
		)
		
		for a,b,c in WIN_LINES:
			if( self.board[a] == self.board[b] == self.board[c] ):
				if(self.board[a] == 'X') : return 1
				if(self.board[a] == 'O') : return -1
		if '.' in self.board : 	return None
		return 0
	
	def getMoves(self):
		l =  []
		for i in range(len(self.board)):
			if(self.board[i] != 'X' and self.board[i] != 'O'):
				l.append((int(i/3), i%3))
		return l
			
	
	def display(self):
		for i in range(0,9,3):
			print(" ".join(self.board[i:i+3]))
		print("\n")


def minmax(state):
	score = state.evaluate()
	if score is not None:
		return score
	
	if state.getCurrentPlayer() == 1:
		best = -float('inf')
		for move in state.getMoves():
			best = max(best, minmax(state.makeMove(move)))
		return best
	else:
		best = float('inf')
		for move in state.getMoves():
			best = min(best, minmax(state.makeMove(move)))
		return best

def bestMove(state):
	if state.getCurrentPlayer() == 1:  # X massimizza
		best_value = -float('inf')
		best_move = None
		for move in state.getMoves():
			value = minmax(state.makeMove(move))
			if value > best_value:
				best_value = value
				best_move = move
	else:  # O minimizza
		best_value = float('inf')
		best_move = None
		for move in state.getMoves():
			value = minmax(state.makeMove(move))
			if value < best_value:
				best_value = value
				best_move = move

	return best_move


state = TicTacToe()
turn = 0


while True:
	if state.getCurrentPlayer() == 1:
		print("Giocatore umano(X)")
	else:
		print("Computer (O)")
		
	state.display()
	
	value = state.evaluate()
	
	if value is not None:
		if value == 1:
			print("Umano vince")
		elif value == -1:
			print("Robot vince")
		else:
			print("Pareggio")
		break
	
	
	if state.getCurrentPlayer() == 1:
		print("Tocca a te umano")
		r = int(input("Riga:"))
		c = int(input("Colonna:"))
		state = state.makeMove((r,c))
	else:
		print("Computer pensa")
		move = bestMove(state)
		state = state.makeMove(move)

		
		
		
