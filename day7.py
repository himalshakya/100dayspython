"""
Hangman game
"""


from art import hangman_logo, hangman_stages
from hangman_words import word_list
import random

VALID_CHOICES = [chr(i) for i in range(97, 123)]
MAX_MISTAKES_ALLOWED = len(hangman_stages)


def print_output(letter_list):
    print(" ".join(letter_list))


def play_game(word):
    used_letters = []
    current_solution = ["_" for _ in range(len(word))]
    remaining_mistakes = MAX_MISTAKES_ALLOWED - 1

    while "_" in current_solution:
        print_output(letter_list=current_solution)
        guess = input("Guess a letter: ").lower()
        if guess not in VALID_CHOICES:
            print("This is not a valid choice.")
            continue
        else:
            if guess in used_letters:
                print(f"{guess} has already been used.")
                continue
            used_letters.append(guess)
            used_letters.sort()

            if guess not in word:
                remaining_mistakes -= 1
            print(hangman_stages[remaining_mistakes])

            if remaining_mistakes <= 0:
                print(f"Sorry, you lose, the word is {word}")
                break

            for index in range(len(word)):
                if word[index] == guess:
                    current_solution[index] = guess

            print("Used words: ")
            print_output(used_letters)

            if "_" not in current_solution:
                print(f"Congratulations, you solution is {word}")
                break


def main():
    string_line = 80 * "*"
    print(string_line)
    print(hangman_logo)
    print(string_line)

    repeat_game = "yes"
    while repeat_game == "yes":
        word = random.choice(word_list)
        play_game(word=word)
        repeat_game = input("Do you want to play again? ")


if __name__ == "__main__":
    main()
