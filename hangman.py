# hangman.py

from random import choice
from string import ascii_lowercase

from rich.console import Console

console = Console()


def select_word():
    with open("words.txt", mode="r") as words:
        word_list = words.readlines()
    return choice(word_list).strip()


def get_player_input(guessed_letters):
    while True:
        player_input = console.input("Guess a letter: ").lower()
        if _validate_input(player_input, guessed_letters):
            return player_input


def _validate_input(player_input, guessed_letter):
    return (
        len(player_input) == 1
        and player_input in ascii_lowercase
        and player_input not in guessed_letter
    )


def join_guessed_letters(guessed_letters):
    return " ".join(sorted(guessed_letters))


def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(letter)
        else:
            current_letters.append("_")
    return " ".join(current_letters)


def draw_hanged_man(wrong_guesses):
    hanged_man = [
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
    ]
    console.print(hanged_man[wrong_guesses])


def pretty_print(hanged_man):
    pass
