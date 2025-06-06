"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgen@gmail.com
"""

import random
import inflect
import time

def secret_number_gen():
    """Return 4 digits number without 0 as first digit"""
    while True:
        secret_num = random.sample(range(10), 4)
        if secret_num[0] != 0:
            secret_num_complete = "".join(
                str(number) for number in secret_num
                )
            return secret_num_complete


def line_printer():
    """Prints aseparator line"""
    print(45 * "-")


def print_intro_text():
    """Prints intro text with basic info about game"""
    print("Hi there!")
    line_printer()    
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    line_printer()


def player_number_input(player_number: str, used_numbers: set):
    """Returns 4 digits number without 0 as first digit,
        prints message if number was just used or
        if contains duplicate digits etc."""
    
    if not player_number.isdigit():
        print("You have to enter number.")
    elif len(player_number) != 4:
        print("Your number has to be 4 digits long.")
    elif player_number[0] == "0":
        print("Your number can´t begin with 0 .")
    elif player_number in used_numbers:
        print("You have already used this number.")
    elif len(set(player_number)) < 4:
        print("Your number contains duplicate digits.")
    else:
        return player_number                    


def bulls_cows_counter(guess,secret):
    """Returns number of bulls and cows"""
    bulls = 0
    cows = 0
    for letter in range(4):
        if guess[letter] == secret[letter]:
            bulls += 1
        elif guess[letter] != secret[letter] and guess[letter] in secret:
            cows += 1
    return bulls, cows


def result_printer(res1,res2):
    """Prints result with correct plural grammar"""
    plur = inflect.engine()
    word_1 = "bull"
    word_2 = "cow"

    print(f"{res1} {plur.plural(word_1,res1)}," 
        f" {res2} {plur.plural(word_2,res2)}")
    

def main_game():
    secret_number = secret_number_gen()
    #print(secret_number) - only for testing
    player_nr = None
    attempts = 1
    used_numbers = set()
    start = time.perf_counter()

    print_intro_text()
    
    while secret_number != player_nr:
        while player_nr == None:
            player_guess = input("Enter a number: ")
            player_nr = player_number_input(player_guess,used_numbers)
            line_printer()  
        
        if player_nr == secret_number:
            elapsed = time.perf_counter() - start
            print(f"Correct, you´ve guessed the"
            f" right number in {attempts} guesses!")
            print(f"It took {elapsed:.2f} seconds.")
            break
            
        else:
            attempts += 1
            used_numbers.add(player_nr)
            result = bulls_cows_counter(player_nr,secret_number)
                    
            result_printer(result[0],result[1])
            player_nr = None

if __name__ == "__main__":
    main_game()


        
  
        

