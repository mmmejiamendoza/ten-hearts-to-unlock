#!/usr/bin/env python3
"""
🎀 TEN HEARTS TO UNLOCK 🎀
A cute, cozy, pink-coquette gauntlet of 10 mini-games.
Win all 10 in a row to unlock... a phone number. 😉

Lose any single game, and it's back to Game 1. No mercy, only cuteness. 🩷

HOW TO CUSTOMIZE:
Everything you'd want to personalize lives in the CONFIG section right below.
Edit those values, then just run:  python3 ten_hearts_to_unlock.py
"""

import random
import time
import os
import sys

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    PINK = Fore.MAGENTA
    LPINK = Fore.LIGHTMAGENTA_EX
    RED = Fore.LIGHTRED_EX
    GREEN = Fore.LIGHTGREEN_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    CYAN = Fore.LIGHTCYAN_EX
    BOLD = Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:
    PINK = LPINK = RED = GREEN = YELLOW = CYAN = BOLD = RESET = ""

MY_SECRET_NUMBER = 10                 # Game 2: pick any number 1-10
WORDLE_WORD = "TULIPS"                # Game 3: any word you like
SCRAMBLE_WORD = "SHADOW"            # Game 4: any word you like
SCRAMBLE_HINTS = [
    "there are games, shows, FANART, and movies",
    "red is associated with this character",
    "keanu reeves played him",
]
HANGMAN_WORD = "PIPLUP"            # Game 9: any word you like

RIDDLES = [  # Game 6: (emoji clue, answer, hint)
    ("💜🔮✨", "twilight sparkle", "magical princess who loves books"),
    ("🐶😎🐤", "snoopy", "its offical name is something people are allergic to"),
    ("🐾🐟🥛", "gato", "the spanish term for this"),
]

MEMORY_SEQUENCE = ["rose", "tulip", "daisy", "lily"]  # Game 7

TWO_TRUTHS = [                        # Game 8 — edit to be about YOU
    "i love drawing",
    "i have always liked ice cream",
    "i have cats",
]
LIE_INDEX = 2  # which statement (1, 2, or 3) is the lie

TRIVIA_QUESTIONS = [                  # Game 10 — "how well do you know me"
    {
        "question": "who is my favorite sonic character?",
        "options": {"A": "Sonic", "B": "Shadow", "C": "Silver"},
        "answer": "B",
    },
    {
        "question": "What hello kitty character do i love?",
        "options": {"A": "hello kitty", "B": "my melody", "C": "cinnamonroll"},
        "answer": "C",
    },
    {
        "question": "what MLP character is my favorite?",
        "options": {"A": "pinkie pie", "B": "twilight sparkle", "C": "applejack"},
        "answer": "B",
    },
]

YOUR_PHONE_NUMBER = "(469) 515-3557"
FINAL_MESSAGE = "Hooray! You passed! Text me! But also do tell me about the game lol 🩷"

# ============================================================
# 🎀 helpers 🎀
# ============================================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause(sec=1.1):
    time.sleep(sec)


def press_enter():
    input(f"\n{LPINK}      (press enter to continue) {RESET}")


def divider():
    print(f"{PINK}{BOLD}" + "𓂃 ⋆｡˚ ♡ ⋆｡˚ ⋆｡˚ ♡ ⋆｡˚ 𓂃" + RESET)


def header(title, game_num):
    clear()
    divider()
    print(f"{PINK}{BOLD}      🎀 GAME {game_num}/10: {title} 🎀{RESET}")
    divider()
    print()


def win_msg(text="Yay!! You did it!! 🎉💗"):
    print(f"\n{GREEN}{BOLD}{text}{RESET}")


def lose_msg(text="Awww, not quite bestie 🥺"):
    print(f"\n{RED}{BOLD}{text}{RESET}")


def award_point(n):
    print(f"\n{YELLOW}✨ You earned point #{n} of 10! ✨{RESET}")
    pause(1.3)


# ============================================================
# 🎀 GAME 1 — Tic Tac Toe Showdown (best of 3 vs AI) 🎀
# ============================================================

def print_board(b):
    def c(i):
        return b[i] if b[i] != " " else str(i + 1)
    print(f"""
     {LPINK}{c(0)} │ {c(1)} │ {c(2)}
    ───┼───┼───
     {c(3)} │ {c(4)} │ {c(5)}
    ───┼───┼───
     {c(6)} │ {c(7)} │ {c(8)}{RESET}
    """)


def check_winner(b):
    lines = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for x, y, z in lines:
        if b[x] == b[y] == b[z] != " ":
            return b[x]
    if " " not in b:
        return "draw"
    return None


def ai_move(b, ai="O", human="X"):
    empties = [i for i, v in enumerate(b) if v == " "]
    # try to win
    for i in empties:
        b2 = b[:]; b2[i] = ai
        if check_winner(b2) == ai:
            return i
    # block human win
    for i in empties:
        b2 = b[:]; b2[i] = human
        if check_winner(b2) == human:
            return i
    return random.choice(empties)


def play_tictactoe_round():
    board = [" "] * 9
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            return winner
        try:
            move = int(input(f"{CYAN}Pick a spot (1-9): {RESET}")) - 1
        except ValueError:
            print("Numbers only, cutie. Try again.")
            continue
        if move not in range(9) or board[move] != " ":
            print("That spot's taken (or not valid). Try again!")
            continue
        board[move] = "X"
        winner = check_winner(board)
        if winner:
            print_board(board)
            return winner
        ai_i = ai_move(board)
        board[ai_i] = "O"


def game_tictactoe():
    header("Tic Tac Toe Showdown", 1)
    print("Best 2 out of 3 rounds against the AI. You're X, AI is O.\n")
    wins = 0
    for r in range(1, 4):
        print(f"{PINK}--- Round {r} ---{RESET}")
        result = play_tictactoe_round()
        if result == "X":
            print(f"{GREEN}You won round {r}! 🎉{RESET}")
            wins += 1
        elif result == "O":
            print(f"{RED}AI won round {r}. 😳{RESET}")
        else:
            print(f"{YELLOW}Round {r} was a draw!{RESET}")
        pause(1)
    return wins >= 2


# ============================================================
# 🎀 GAME 2 — Guess My Number (1-10, 3 guesses) 🎀
# ============================================================

def game_guess_number():
    header("Guess My Number", 2)
    print("I'm thinking of a number between 1 and 10. You have 3 guesses!\n")
    for attempt in range(1, 4):
        try:
            guess = int(input(f"{CYAN}Guess #{attempt}: {RESET}"))
        except ValueError:
            print("Numbers only please!")
            continue
        if guess == MY_SECRET_NUMBER:
            return True
        elif guess < MY_SECRET_NUMBER:
            print(f"{YELLOW}Higher! 📈{RESET}")
        else:
            print(f"{YELLOW}Lower! 📉{RESET}")
    print(f"\nThe number was {MY_SECRET_NUMBER}.")
    return False


# ============================================================
# 🎀 GAME 3 — Love Wordle (2 hints allowed) 🎀
# ============================================================

def wordle_feedback(guess, word):
    result = []
    for i, ch in enumerate(guess):
        if ch == word[i]:
            result.append(f"{GREEN}{ch.upper()}{RESET}")
        elif ch in word:
            result.append(f"{YELLOW}{ch.upper()}{RESET}")
        else:
            result.append(f"{Fore.LIGHTBLACK_EX if 'Fore' in dir() else ''}{ch.upper()}{RESET}")
    return " ".join(result)


def game_wordle():
    word = WORDLE_WORD.lower()
    header("Love Wordle", 3)
    max_guesses = len(word) + 2
    hints_left = 2
    print(f"Guess the {len(word)}-letter word! You have {max_guesses} guesses.")
    print("Type 'hint' instead of a guess to use one of your 2 hints.\n")
    revealed = ["_"] * len(word)
    for attempt in range(1, max_guesses + 1):
        guess = input(f"{CYAN}Guess #{attempt} (or 'hint'): {RESET}").strip().lower()
        if guess == "hint":
            if hints_left <= 0:
                print("No hints left, sorry cutie!")
                continue
            unrevealed = [i for i, ch in enumerate(revealed) if ch == "_"]
            if unrevealed:
                i = random.choice(unrevealed)
                revealed[i] = word[i]
                hints_left -= 1
                print(f"{PINK}Hint: {' '.join(revealed).upper()}{RESET}")
            continue
        if len(guess) != len(word):
            print(f"Word must be {len(word)} letters!")
            continue
        print(wordle_feedback(guess, word))
        if guess == word:
            return True
    print(f"\nThe word was: {word.upper()}")
    return False


# ============================================================
# 🎀 GAME 4 — Scrambled Secret (word scramble, 3 hints) 🎀
# ============================================================

def scramble(word):
    letters = list(word)
    scrambled = word
    while scrambled == word:
        random.shuffle(letters)
        scrambled = "".join(letters)
    return scrambled


def game_scramble():
    word = SCRAMBLE_WORD.upper()
    header("Scrambled Secret", 4)
    scrambled = scramble(word)
    print(f"Unscramble this word: {BOLD}{PINK}{scrambled}{RESET}")
    print(f"You have 5 guesses and {len(SCRAMBLE_HINTS)} hints (type 'hint').\n")
    hints_used = 0
    for attempt in range(1, 6):
        guess = input(f"{CYAN}Guess #{attempt} (or 'hint'): {RESET}").strip().upper()
        if guess == "HINT":
            if hints_used >= len(SCRAMBLE_HINTS):
                print("No more hints, love!")
                continue
            print(f"{PINK}Hint: {SCRAMBLE_HINTS[hints_used]}{RESET}")
            hints_used += 1
            continue
        if guess == word:
            return True
        print("Nope, try again!")
    print(f"\nThe word was: {word}")
    return False


# ============================================================
# 🎀 GAME 5 — Rock Paper Scissors Hearts (best of 3) 🎀
# ============================================================

def game_rps():
    header("Rock Paper Scissors Hearts", 5)
    print("Best of 3 against the AI! (rock/paper/scissors)\n")
    choices = ["rock", "paper", "scissors"]
    wins = losses = 0
    round_num = 1
    while wins < 2 and losses < 2:
        user = input(f"{CYAN}Round {round_num} - your move: {RESET}").strip().lower()
        if user not in choices:
            print("Type rock, paper, or scissors!")
            continue
        ai = random.choice(choices)
        print(f"AI chose: {ai}")
        if user == ai:
            print(f"{YELLOW}Tie! Replay this round.{RESET}")
            continue
        beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
        if beats[user] == ai:
            print(f"{GREEN}You win this round!{RESET}")
            wins += 1
        else:
            print(f"{RED}AI wins this round.{RESET}")
            losses += 1
        round_num += 1
        pause(0.8)
    return wins > losses


# ============================================================
# 🎀 GAME 6 — Emoji Riddle Garden 🎀
# ============================================================

def game_riddles():
    header("Emoji Riddle Garden", 6)
    print("Guess the word from the emoji clue! One hint each if you need it.\n")
    correct = 0
    for emoji, answer, hint in RIDDLES:
        print(f"{PINK}{emoji}{RESET}")
        guess = input(f"{CYAN}Your answer: {RESET}").strip().lower()
        if guess != answer:
            print(f"{PINK}Hint: {hint}{RESET}")
            guess = input(f"{CYAN}Try again: {RESET}").strip().lower()
        if guess == answer:
            print(f"{GREEN}Correct!{RESET}\n")
            correct += 1
        else:
            print(f"{RED}It was '{answer}'.{RESET}\n")
    return correct >= 2


# ============================================================
# 🎀 GAME 7 — Memory Bouquet 🎀
# ============================================================

FLOWER_EMOJI = {"rose": "🌹", "tulip": "🌷", "daisy": "🌼", "lily": "🌸"}

def game_memory():
    header("Memory Bouquet", 7)
    seq = MEMORY_SEQUENCE
    print("Memorize this bouquet order:\n")
    print("  " + "  ".join(f"{FLOWER_EMOJI.get(f,'🌸')} {f}" for f in seq))
    pause(3)
    clear()
    header("Memory Bouquet", 7)
    print("Now type the flowers back IN ORDER, separated by spaces.")
    print(f"(options were: {', '.join(FLOWER_EMOJI.keys())})\n")
    answer = input(f"{CYAN}Your order: {RESET}").strip().lower().split()
    if answer == seq:
        return True
    print(f"\nThe correct order was: {' '.join(seq)}")
    print("One more try...")
    answer2 = input(f"{CYAN}Your order: {RESET}").strip().lower().split()
    return answer2 == seq


# ============================================================
# 🎀 GAME 8 — Two Truths and a Lie 🎀
# ============================================================

def game_two_truths():
    header("Two Truths and a Lie", 8)
    print("Which one is the LIE?\n")
    for i, s in enumerate(TWO_TRUTHS, start=1):
        print(f"  {i}. {s}")
    for attempt in range(2):
        try:
            guess = int(input(f"\n{CYAN}Your guess (1-3): {RESET}"))
        except ValueError:
            print("Numbers only!")
            continue
        if guess == LIE_INDEX:
            return True
        print(f"{RED}Nope, that one's true!{RESET}")
    return False


# ============================================================
# 🎀 GAME 9 — Wilting Rose Hangman 🎀
# ============================================================

ROSE_STAGES = [
    "🌹  (full bloom)",
    "🌹  (still lovely)",
    "🥀  (petals drooping)",
    "🥀  (wilting...)",
    "🥀  (almost gone...)",
    "🥀💔 (wilted completely)",
]

def game_hangman():
    word = HANGMAN_WORD.upper()
    header("Wilting Rose Hangman", 9)
    guessed = set()
    wrong = 0
    max_wrong = len(ROSE_STAGES) - 1
    while wrong < max_wrong:
        display = " ".join(c if c in guessed else "_" for c in word)
        print(f"\n{ROSE_STAGES[wrong]}")
        print(f"Word: {display}")
        if "_" not in display:
            return True
        letter = input(f"{CYAN}Guess a letter: {RESET}").strip().upper()
        if len(letter) != 1 or not letter.isalpha():
            print("Just one letter please!")
            continue
        if letter in guessed:
            print("Already guessed that one!")
            continue
        guessed.add(letter)
        if letter not in word:
            wrong += 1
            print(f"{RED}Not in the word!{RESET}")
        else:
            print(f"{GREEN}Yes!{RESET}")
    print(f"\n{ROSE_STAGES[-1]}")
    print(f"The word was: {word}")
    return False


# ============================================================
# 🎀 GAME 10 — Final Trivia: How Well Do You Know Me? 🎀
# ============================================================

def game_trivia():
    header("How Well Do You Know Me?", 10)
    print("The final heart! Get at least 2 of 3 right.\n")
    correct = 0
    for q in TRIVIA_QUESTIONS:
        print(f"{BOLD}{q['question']}{RESET}")
        for k, v in q["options"].items():
            print(f"  {k}) {v}")
        ans = input(f"{CYAN}Your answer: {RESET}").strip().upper()
        if ans == q["answer"]:
            print(f"{GREEN}Correct!{RESET}\n")
            correct += 1
        else:
            print(f"{RED}Nope, it was {q['answer']}.{RESET}\n")
    return correct >= 2


# ============================================================
# 🎀 finale 🎀
# ============================================================

def show_finale():
    clear()
    divider()
    print(f"""
{PINK}{BOLD}
        (◍•ᴗ•◍)❤        🎀 YOU DID IT 🎀

     You won all 10 hearts. Here's your prize:
{RESET}
{LPINK}{BOLD}          📱  {YOUR_PHONE_NUMBER}  📱{RESET}
{PINK}
        {FINAL_MESSAGE}
{RESET}
""")
    divider()


def reset_message():
    clear()
    divider()
    print(f"""
{RED}{BOLD}
        (╥﹏╥)  Awww, so close!

     That wasn't quite it — back to Game 1 we go!
     Don't worry, cuteness takes practice. 🩷
{RESET}
""")
    divider()
    pause(2)


# ============================================================
# 🎀 main loop 🎀
# ============================================================

GAMES = [
    game_tictactoe,
    game_guess_number,
    game_wordle,
    game_scramble,
    game_rps,
    game_riddles,
    game_memory,
    game_two_truths,
    game_hangman,
    game_trivia,
]


def intro():
    clear()
    divider()
    print(f"""
{PINK}{BOLD}
      🎀 TEN HEARTS TO UNLOCK 🎀

   Win 10 tiny games in a row to unlock a secret.
   Lose even one, and we start allllll the way over.

   Ready?
{RESET}
""")
    divider()
    press_enter()


def main():
    intro()
    index = 0
    while index < len(GAMES):
        result = GAMES[index]()
        if result:
            award_point(index + 1)
            index += 1
        else:
            lose_msg()
            reset_message()
            index = 0
    show_finale()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{PINK}Bye for now! 🎀{RESET}")
        sys.exit(0)