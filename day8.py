"""
Casear Cipher
"""

from art import caesar_cipher

LOWERCASE_LETTER = [chr(i) for i in range(97, 123)]
LETTERS_COUNT = len(LOWERCASE_LETTER)
DOUBLE_LOWERCASE_LETTER = 2 * LOWERCASE_LETTER
UPPERCASE_LETTER = [chr(i) for i in range(65, 91)]
DOUBLE_UPPERCASE_LETTER = 2 * UPPERCASE_LETTER


def process(word, offset, encrpyt=True):
    letters = list(word)

    for index in range(len(letters)):
        current_letter = letters[index]
        if current_letter in LOWERCASE_LETTER:
            if encrpyt:
                letter_index = LOWERCASE_LETTER.index(current_letter)
                letters[index] = DOUBLE_LOWERCASE_LETTER[letter_index + offset]
            else:
                letter_index = (
                    DOUBLE_LOWERCASE_LETTER.index(current_letter) + LETTERS_COUNT
                )
                letters[index] = DOUBLE_LOWERCASE_LETTER[letter_index - offset]

        if current_letter in UPPERCASE_LETTER:
            if encrpyt:
                letter_index = UPPERCASE_LETTER.index(current_letter)
                letters[index] = DOUBLE_UPPERCASE_LETTER[letter_index + offset]
            else:
                letter_index = (
                    DOUBLE_UPPERCASE_LETTER.index(current_letter) + LETTERS_COUNT
                )
                letters[index] = DOUBLE_UPPERCASE_LETTER[letter_index - offset]
    return letters


def main():
    string_line = 80 * "*"
    print(string_line)
    print(caesar_cipher)
    print(string_line)

    repeat_game = "yes"
    while repeat_game == "yes":
        encrpt_question = input("Do you want to encrypt/decrypt? ")
        word = input("What is the word? ")
        offset = int(input("Enter the offset value: "))

        encrpyt = True
        if encrpt_question == "decrypt":
            encrpyt = False

        answer = "".join(process(word=word, offset=offset, encrpyt=encrpyt))
        print(f"The {encrpt_question}ed word is {answer}.")
        repeat_game = input("Do you want to process again? ")

    # print(process(word="hello", offset=5))
    # print(process(word="mjqqt", offset=5, encrpyt=False))
    # print(process(word="test 123 abc", offset=5))
    # print(process(word="Hello", offset=5))
    # print(process(word="Mjqqt", offset=5, encrpyt=False))


if __name__ == "__main__":
    main()
