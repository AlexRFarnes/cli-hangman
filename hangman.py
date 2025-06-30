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
