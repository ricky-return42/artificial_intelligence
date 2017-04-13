import sys
import numpy as np 


class game:

	def __init__(self):
		self.game_id = 1


	def create_board(self):
		board = np.chararray((3,3))
		board[:] = ''
		return board
		

	def create_win_combo(self,board):
		return [board[0], board[1], board[2], board[:,0], board[:,1], board[:,2], board.diagonal(), np.fliplr(board).diagonal()]

if __name__ == '__main__':
	board = game().create_board()
	wincomb = game().create_win_combo(board)
	print wincomb
	