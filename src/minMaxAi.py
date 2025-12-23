class MinMaxAi:
	def minMax(self, state):
		score = state.evaluate()
		if score is not None: return score
		
		if state.getCurrentPlayer() == 1: 
			best = -float('inf')
			for move in state.getMoves():	
				best = max(best , self.minMax(state.makeMove(move)))
			return best
		else:
			best = float('inf')
			for move in state.getMoves():
				best = min(best, self.minMax(state.makeMove(move)))
			return best
	
	def bestMove(self, state):
		if state.getCurrentPlayer() == 1:
			best_value = -float('inf')
			best_move = None
			for move in state.getMoves():
				value  = self.minMax(state.makeMove(move))
				if value > best_value:
					best_value = value
					best_move = move
		else:
			best_value = float('inf')
			best_move = None
			for move in state.getMoves(): 
				value = self.minMax(state.makeMove(move))
				if value < best_value:
					best_value = value
					best_move = move
		return best_move
	
