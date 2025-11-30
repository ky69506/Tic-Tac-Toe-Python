import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ============================
#          MENU
# ============================
class Menu:
    @staticmethod
    def main_menu():
        while True:
            choice = input("1. Start Game\n2. Quit\nChoose (1-2): ")
            if choice in ("1", "2"):
                return int(choice)
            print("Invalid choice!")

    @staticmethod
    def end_menu():
        while True:
            choice = input("1. Play Again\n2. Quit\n3. Show Score\nChoose (1-2-3): ")
            if choice in ("1", "2", "3"):
                return int(choice)
            print("Invalid choice!")



# ============================
#          PLAYER
# ============================
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.score = 0



# ============================
#          BOARD
# ============================
class Board:
    def __init__(self):
        self.reset()

    def reset(self):
        self.board = [" " for _ in range(9)]

    def display(self):
        clear_screen()
        print()
        for i in range(0, 9, 3):
            print(f" {self.cell(i)} | {self.cell(i+1)} | {self.cell(i+2)} ")
            if i < 6:
                print("---+---+---")
        print()

    def cell(self, index):
        return self.board[index] if self.board[index] != " " else str(index+1)

    def is_empty(self, index):
        return self.board[index] == " "

    def place_symbol(self, index, symbol):
        self.board[index] = symbol

    def is_full(self):
        return all(cell != " " for cell in self.board)

    def check_win(self, symbol):
        win_patterns = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in win_patterns:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] == symbol:
                return True
        return False



# ============================
#          GAME LOGIC
# ============================
class Game:
    def __init__(self):
        self.board = Board()

    def setup_players(self):
        print("\nPlayer 1:")
        p1_name = self.ask_name()
        p1_symbol = self.ask_symbol()

        print("\nPlayer 2:")
        p2_name = self.ask_name()

        # Player 2 can't pick same symbol
        while True:
            p2_symbol = self.ask_symbol()
            if p2_symbol != p1_symbol:
                break
            print("Symbol already taken!")

        self.player1 = Player(p1_name, p1_symbol)
        self.player2 = Player(p2_name, p2_symbol)
        self.current = self.player1

    def ask_name(self):
        while True:
            name = input("Enter your name: ")
            if len(name) >= 2 and name.isalpha():
                return name.capitalize()
            print("Invalid name!")

    def ask_symbol(self):
        while True:
            s = input("Choose symbol (1 character letter): ")
            if len(s) == 1 and s.isalpha():
                return s.upper()
            print("Invalid symbol!")

    def switch_player(self):
        self.current = self.player2 if self.current == self.player1 else self.player1

    def play_turn(self):
        while True:
            try:
                choice = int(input(f"{self.current.name}'s turn ({self.current.symbol}): ")) - 1
                if choice not in range(9):
                    print("Out of range!")
                    continue
                if not self.board.is_empty(choice):
                    print("Cell already used!")
                    continue
                self.board.place_symbol(choice, self.current.symbol)
                return
            except ValueError:
                print("Invalid input!")

    def game_loop(self):
        self.board.display()

        while True:
            self.play_turn()
            self.board.display()

            # Check win
            if self.board.check_win(self.current.symbol):
                print(f"{self.current.name} wins!")
                self.current.score += 1
                return

            # Check draw
            if self.board.is_full():
                print("Draw!")
                return

            self.switch_player()

    def start(self):
        while True:
            if Menu.main_menu() == 2:
                print("Exiting game…")
                return

            clear_screen()
            self.setup_players()

            while True:
                self.board.reset()
                self.game_loop()

                again = Menu.end_menu()
                if again == 2:
                    break
                elif again == 3:
                    clear_screen()
                    print(f"\nScores:\n{self.player1.name}: {self.player1.score}\n{self.player2.name}: {self.player2.score}\n")
                    input("Press Enter to continue… ")

            print("Returning to main menu…")


# ============================
#         RUN GAME
# ============================
Game().start()