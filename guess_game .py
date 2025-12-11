import random
import time
import os
import sys

# ANSI Colors for styling
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear_screen():
    """Clear terminal screen"""
    os.system("cls" if os.name == "nt" else "clear")

def sound_win():
    """Play win sound (Windows only)"""
    if os.name == "nt":
        try:
            import winsound
            winsound.Beep(800, 200)
            winsound.Beep(1000, 200)
            winsound.Beep(1200, 300)
        except:
            pass  # Ignore if winsound not available

def sound_wrong():
    """Play wrong guess sound (Windows only)"""
    if os.name == "nt":
        try:
            import winsound
            winsound.Beep(400, 150)
        except:
            pass

def stylish_print(text, delay=0.02):
    """Print text with animation effect"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def game_logo():
    """Display ASCII game logo"""
    logo = f"""
{CYAN}{BOLD}
███    ██  ██████  ██████  ██████  ███    ███ 
████   ██ ██    ██ ██   ██ ██   ██ ████  ████ 
██ ██  ██ ██    ██ ██████  ██████  ██ ████ ██ 
██  ██ ██ ██    ██ ██   ██ ██   ██ ██  ██  ██ 
██   ████  ██████  ██████  ██   ██ ██      ██ 
{RESET}
"""
    print(logo)

def choose_mode():
    """Select difficulty mode"""
    print(f"{YELLOW}{BOLD}Choose Difficulty Mode:{RESET}")
    print("1. Easy (1–20)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")
    print("4. Impossible (1–500)")
    
    while True:
        choice = input(f"{CYAN}👉 Select mode (1-4): {RESET}")
        if choice in ["1","2","3","4"]:
            return int(choice)
        print(f"{RED}❌ Invalid choice! Enter 1, 2, 3, or 4.{RESET}")

def get_range(mode):
    """Return max number based on mode"""
    return {1: 20, 2: 50, 3: 100, 4: 500}[mode]

def modern_guess_game():
    """Main game function"""
    clear_screen()
    game_logo()

    mode = choose_mode()
    max_num = get_range(mode)
    number = random.randint(1, max_num)
    attempts = 0

    stylish_print(f"{CYAN}{BOLD}🎮 Welcome to the Modern Guessing Game!{RESET}", 0.01)
    stylish_print(f"{YELLOW}I'm thinking of a number between 1 and {max_num}...{RESET}", 0.01)
    stylish_print(f"Try to guess it! 🚀\n", 0.01)

    while True:
        guess_input = input(f"{CYAN}👉 Enter your guess: {RESET}")
        if not guess_input.isdigit():
            print(f"{RED}❌ Enter a valid number!{RESET}")
            sound_wrong()
            continue

        guess = int(guess_input)
        attempts += 1

        if guess < number:
            print(f"{YELLOW}📉 Too low! Try again.{RESET}")
            sound_wrong()
        elif guess > number:
            print(f"{YELLOW}📈 Too high! Try again.{RESET}")
            sound_wrong()
        else:
            stylish_print(f"\n{GREEN}{BOLD}🎉 CORRECT! You guessed it in {attempts} attempts!{RESET}", 0.01)
            sound_win()
            break

if __name__ == "__main__":
    modern_guess_game()