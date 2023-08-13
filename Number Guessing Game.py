import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.lower_limit = 1
        self.upper_limit = 100
        self.target_number = random.randint(self.lower_limit, self.upper_limit)
        self.attempts = 0
        self.max_attempts = 7

        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", command=self.play_again, state=tk.DISABLED)
        self.play_again_button.pack(pady=5)

    def check_guess(self):
        try:
            player_guess = int(self.entry.get())
            self.attempts += 1

            if player_guess < self.target_number:
                result_text = "Higher!"
            elif player_guess > self.target_number:
                result_text = "Lower!"
            else:
                result_text = f"Congratulations! You guessed the number {self.target_number} in {self.attempts} attempts."
                self.guess_button.config(state=tk.DISABLED)
                self.play_again_button.config(state=tk.NORMAL)

            if self.attempts >= self.max_attempts:
                result_text = f"Sorry, you've reached the maximum number of attempts. The number was {self.target_number}."

            self.result_label.config(text=result_text)
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def play_again(self):
        self.target_number = random.randint(self.lower_limit, self.upper_limit)
        self.attempts = 0
        self.result_label.config(text="")
        self.guess_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED)
        self.entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()