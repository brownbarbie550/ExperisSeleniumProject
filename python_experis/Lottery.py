import random


class Lottery:

    def __init__(self, raffle_range, max_win):
        self.UP = 45
        self.LOW = 1
        self.raffle_range = raffle_range
        self.num_list = []
        self.max_win = max_win

    def nums_raffle(self):
        """Generates 6 unique random numbers between 1 and UP."""
        self.num_list = random.sample(range(self.LOW, self.UP + 1), 6)
        print(f"Drawn numbers: {self.num_list}")

    def max_prize(self):
        """Returns the maximum prize."""
        return f"The maximum win amount is: {self.max_win}"

    def __str__(self):
        """Returns a string representing the drawn numbers."""
        return f"The raffled numbers are: {self.num_list}"

    def checks_guesses(self, user_guess):
        """Returns a list of correct guesses (numbers present in the draw)."""
        correct_guesses = [guess for guess in user_guess if guess in self.num_list]
        return correct_guesses

    def calc_correct_guess(self, correct_guesses):
        """Calculates the prize based on the number of correct guesses."""
        num_correct = len(correct_guesses)

        if num_correct <= 1:
            return 0  # No prize
        elif 2 <= num_correct <= 5:
            return (self.max_win * num_correct) // 6  # Proportional prize
        elif num_correct == 6:
            return self.max_win  # Full prize for 6 correct guesses
        else:
            return 0  # Just in case of invalid guesses


# Main program
def main():
    # Create a lottery object
    lottery = Lottery(45, 1000)


    # Print the max win amount
    print(lottery.max_prize())

    # Initialize list for user guesses
    user_guesses = []

    # Collect 6 guesses from the user
    for i in range(6):
        guess_num = input(f"Enter guess {i + 1} (between 1 and 45): ")

        # Validate the input
        if not guess_num.isdigit():
            print("You have been disqualified due to invalid guesses.")
            return  # Exit the function if the user enters a non-numeric value
        guess_num = int(guess_num)

        if guess_num < 1 or guess_num > 45:  # Check if the guess is in the valid range
            print("Invalid number, you are disqualified from the lottery game due to wrong guesses.")
            return  # Exit the function if the guess is out of range

        user_guesses.append(guess_num)

    # Check the correct guesses
    correct_guesses = lottery.checks_guesses(user_guesses)
    print(f"Correct guesses: {correct_guesses}")

    #Draw 6 numbers
    lottery.nums_raffle()

    # Calculate and print the prize
    prize = lottery.calc_correct_guess(correct_guesses)
    print(f"You won {prize} money.")


# Run the main program
if __name__ == "__main__":
    main()
