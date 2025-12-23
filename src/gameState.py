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
	def makeMove(self,move):
		pass
