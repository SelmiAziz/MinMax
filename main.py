from ticTacToe import TicTacToe
from minMaxAi import MinMaxAi

choice = input("Choice X or O : ")

c = 1

if choice == 'O':	
	c = -1

g = TicTacToe(None, c)
m = MinMaxAi()
g.display()




turn = 1
while True: 
	r = g.evaluate()
	if r is not None:
		if r == 1: 
			print("X has win!!")
		elif r == -1:
			print("O has win!!")
		else:
			print("Draw!!") 
		break
	
	if turn == 1:
		print("It is your turn")
		r = int(input("Select a raw"))
		c = int(input("Select a colon"))
		g = g.makeMove((r,c))
		turn = -1
	else:
		print("It is robot turn")
		move = m.bestMove(g)
		g = g.makeMove(move)
		turn = 1
	g.display()
	


