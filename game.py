import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.guesses_left = 5

        self.label = tk.Label(master, text="Guess the number (between 1 and 100):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.check_guess)
        self.submit_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.entry.delete(0, tk.END)

        if guess == self.secret_number:
            self.result_label.config(text="Congratulations! You guessed the number.")
            self.submit_button.config(state=tk.DISABLED)
        else:
            self.guesses_left -= 1
            if self.guesses_left == 0:
                self.result_label.config(text=f"Sorry, you ran out of guesses. The number was {self.secret_number}.")
                self.submit_button.config(state=tk.DISABLED)
            else:
                if guess < self.secret_number:
                    self.result_label.config(text=f"Try a higher number. Guesses left: {self.guesses_left}")
                else:
                    self.result_label.config(text=f"Try a lower number. Guesses left: {self.guesses_left}")


def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
