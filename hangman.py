# hangman.py

from random import choice
from string import ascii_lowercase

from rich.console import Console

MAX_INCORRECT_GUESSES = 6

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


def join_guessed_letters(target_word, guessed_letters):
    styled_guessed_letters = []
    for letter in sorted(guessed_letters):
        if letter in target_word:
            styled_guessed_letters.append(f"[blue on green]{letter}[/]")
        else:
            styled_guessed_letters.append(f"[red]{letter}[/]")
    return " ".join(styled_guessed_letters)


def build_guessed_word(target_word, guessed_letters):
    current_letters = []
    for letter in target_word:
        if letter in guessed_letters:
            current_letters.append(f"[green]{letter}[/]")
        else:
            current_letters.append("[dim]_[/]")
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


def game_over(wrong_guesses, target_word, guessed_letters):
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        return True
    if set(target_word) <= guessed_letters:
        return True
    return False


def print_header(headline):
    console.rule(f"[bold blue]:video_game: {headline} :video_game:[/]\n")


if __name__ == "__main__":
    # Initial setup
    target_word = select_word()
    guessed_letters = set()
    guessed_word = build_guessed_word(target_word, guessed_letters)
    wrong_guesses = 0
    print_header("Welcome to Hangman!")

    # Game loop
    while not game_over(wrong_guesses, target_word, guessed_letters):
        draw_hanged_man(wrong_guesses)
        console.print(f"Your word is: {guessed_word}")
        console.print(
            f"Current guessed letters: {join_guessed_letters(target_word, guessed_letters)}\n"
        )
        player_guess = get_player_input(guessed_letters)
        if player_guess in target_word:
            console.print(":confetti_ball: [green]Great guess![/] :confetti_ball:")
        else:
            console.print(":boom: [red]Sorry, it's not there[/] :boom:")
            wrong_guesses += 1
        guessed_letters.add(player_guess)
        guessed_word = build_guessed_word(target_word, guessed_letters)

    # Game over
    draw_hanged_man(wrong_guesses)
    if wrong_guesses == MAX_INCORRECT_GUESSES:
        console.print(
            ":disappointed_face: [red]Sorry, you lost![/] :disappointed_face:"
        )
    else:
        console.print(
            ":trophy: [bold green]Congrats![/] [green]You did it![/] :trophy:"
        )
    console.print(f"Your word was: {target_word}")
