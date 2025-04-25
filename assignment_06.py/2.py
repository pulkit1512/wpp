import random

class Rock_paper_scissors:
    def __init__(self, rounds):
        self.rounds = rounds
        self.current_round = 0
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        return random.choice(self.choices)

    def play_round(self, user_choice):
        if user_choice not in self.choices:
            return "Invalid choice."

        computer_choice = self.get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.user_wins += 1
            print(self.user_wins)
            return "You win!"
        else:
            self.computer_wins += 1
            print(self.computer_wins)
            return "Computer wins!"

# Example usage
game = Rock_paper_scissors(3)
print(game.play_round("rock"))
