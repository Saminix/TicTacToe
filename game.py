
#A Simple TicTacToe game.

import random
board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

choice = ["O", "X"]

moves_list = []
board_list = [0,1,2,3,4,5,6,7,8]

class TicTacToe:
    def __init__(self):
        self.board = ['_' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        print(self.board[0] + "|" + self.board[1] + "|" + self.board[2])
        print(self.board[3] + "|" + self.board[4] + "|" + self.board[5])
        print(self.board[6] + "|" + self.board[7] + "|" + self.board[8])


    def update_board(self, square, letter):
        if self.board[square] == "_":
            self.board[square] = letter
            return True
        return False

    def is_draw(self):
        return "_" not in self.board

    def is_win(self):
        winning_patterns = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]
        ]

        for patterns in winning_patterns:
            a,b,c = patterns
            if self.board[a] == self.board[b] == self.board[c] != "_":
                return True
        return False





class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        move = random.choice(board_list)
        while move in moves_list:
            move = random.choice(board_list)
        moves_list.append(move)
        game.update_board(move, self.letter)


    def get_choice(self):
        Choice = random.choice(choice)
        self.letter = Choice


class AIPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        possible_moves = [i for i, spot in enumerate(game.board) if spot == "_"]


        for move in possible_moves:
            game.board[move] = self.letter
            if game.is_win():
                game.board[move] = "_"
                game.update_board(move, self.letter)
                return
            game.board[move] = "_"


        opponent = "O" if self.letter == "X" else "X"
        for move in possible_moves:
            game.board[move] = opponent
            if game.is_win():
                game.board[move] = "_"
                game.update_board(move, self.letter)
                return
            game.board[move] = "_"


        if 4 in possible_moves:
            game.update_board(4, self.letter)
            return


        corners = [i for i in [0, 2, 6, 8] if i in possible_moves]
        if corners:
            move = random.choice(corners)
            game.update_board(move, self.letter)
            return

        move = random.choice(possible_moves)
        game.update_board(move, self.letter)


    def get_choice(self):
        Choice = random.choice(choice)
        self.letter = Choice



class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        move = int(input("Enter your move (0-8): "))
        while move in moves_list:
            move = int(input("Move is taken. Enter Another: "))
        moves_list.append(move)
        game.update_board(move, self.letter)


    def get_choice(self, computer_choice):
        if computer_choice == "X":
            self.letter = "O"
        else:
            self.letter = "X"
        return self.letter



if __name__ == "__main__":
    print("Welcome to TicTacToe: ")
    tic = TicTacToe()

    ai = AIPlayer("O")
    human = HumanPlayer("X")

    tic.print_board()

    while True:

        human.get_move(tic)

        if tic.is_win():
            print("Human wins!")
            break
        if tic.is_draw():
            print("It's a draw!")
            break

        ai.get_move(tic)
        tic.print_board()
        if tic.is_win():
            print("AI wins!")
            break
        if tic.is_draw():
            print("It's a draw!")
            break

