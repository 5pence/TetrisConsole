import numpy as np


class Tetris:

    current_move = ''

    pieces = {'O': [[4, 14, 15, 5]],
              'I': [[4, 14, 24, 34], [3, 4, 5, 6]],
              'S': [[5, 4, 14, 13], [4, 14, 15, 25]],
              'Z': [[4, 5, 15, 16], [5, 15, 14, 24]],
              'L': [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
              'J': [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
              'T': [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]}

    moves = {'left': [-1, 1, 0],
             'right': [1, 1, 0],
             'down': [0, 1, 0],
             'rotate': [0, 1, 1]}
    base_board = np.array([])
    current_board = np.array([])
    flag = False

    def __init__(self, size):
        self.m, self.n = map(int, size.split())
        self.base_board = np.array(self.n * self.m * ['-']).reshape((self.n, self.m))
        self.current_board = self.base_board.copy()

    def move(self, inp):
        self.current_move = inp
        if inp in self.moves:
            return self.moves[inp]
        if inp == 'exit':
            return inp

    def play(self):
        self.pprint(self.current_board)
        y, z, r = 0, 0, 0
        piece = ''
        while True:
            letter = self.get_letter_input(self)
            if letter in self.pieces.keys():
                y, z, r = 0, 0, 0
                piece = letter
                grid = self.current_board.copy()
                for n in self.pieces[piece][r]:
                    zz = int(n / self.m) + z
                    yy = n % self.m + y
                    grid[zz][yy] = '0'
                self.pprint(grid)
                continue

            # check the piece is in static
            is_static = False
            for n in self.pieces[piece][r]:
                zz = int(n / self.m) + z + 1
                yy = n % self.m + y
                if zz == self.n or self.current_board[zz][yy] == '0':
                    is_static = True
                    break
            if is_static:
                for n in self.pieces[piece][r]:
                    zz = int(n / self.m) + z
                    yy = n % self.m + y
                    self.current_board[zz][yy] = '0'
                if '0' in list(self.current_board[0]):
                    self.pprint(self.current_board)
                    print("\nGame Over!")
                    break

            if letter == 'break':
                for row in range(self.n):
                    if '-' not in list(self.current_board[row]):
                        self.current_board[1:row+1] = self.current_board[:row]
                        self.current_board[0] = np.array(['-']*self.m)
                self.pprint(self.current_board)
                continue

            if letter == 'exit':
                break
            else:
                move = self.move(letter)
                iy, iz, ir = move
                # check move is possible
                y1 = y + iy
                z1 = z + iz
                r1 = (r+ir) % len(self.pieces[piece])
                is_move = True
                for n in self.pieces[piece][r1]:
                    zz = int(n / self.m) + z1
                    yy = n % self.m + y1
                    if zz >= self.n or 0 > yy or yy >= self.m:
                        is_move = False
                        break
                    if self.current_board[zz][yy] == '0':
                        is_move = False
                        break
                if is_move:
                    y = y1
                    z = z1
                    r = r1
                grid = self.current_board.copy()
                for n in self.pieces[piece][r]:
                    zz = int(n / self.m) + z
                    yy = n % self.m + y
                    grid[zz][yy] = '0'
                self.pprint(grid)

    @staticmethod
    def pprint(grid):
        print()
        for i in grid:
            print(*i)

    @staticmethod
    def get_letter_input(self):
        str = input()
        if str == 'piece':
            return input()
        return str

# replace play to play_piece and add fuct play that orch the turns


if __name__ == '__main__':
    tetris = Tetris(input())
    tetris.play()
