"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgen@gmail.com
"""

import random
import inflect
import time

def secret_number_gen():
    while True:
        secret_num = random.sample(range(10), 4)
        if secret_num[0] != 0:
            secret_num_complete = "".join(str(number) for number in secret_num) 
        return secret_num_complete


def line_printer():
    print(45 * "-")


def print_intro_text():
    print("Hi there!")
    line_printer()    
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    line_printer()


def player_number_input(used_numbers):
    while True:
        player_number = input("Enter a number: ")
        if not player_number.isdigit():
            print("Your have to enter number.")
        elif len(player_number) != 4:
            print("Your number have to be 4 digits long.")
        elif player_number[0] == "0":
            print("Your number can´t begin with 0 .")
        elif player_number in used_numbers:
            print("You have already used this number.")
        elif len(set(player_number)) < 4:
            print("Your number contains duplicate digits.")
        else:
            return player_number                    


def bulls_cows_counter(b,c):
    bulls = 0
    cows = 0
    for letter in range(4):
        if b[letter] == c[letter]:
            bulls += 1
        elif b[letter] != c[letter] and b[letter] in c:
            cows += 1
    return bulls, cows


def main_game():
    secret_number = secret_number_gen()
    print(secret_number)
    player_nr = str()
    attempts = 1
    used_numbers = set()
    start = time.perf_counter()

    print_intro_text()

    while secret_number != player_nr:
        player_nr = player_number_input(used_numbers)
        line_printer()
        
        if player_nr == secret_number:
            elapsed = time.perf_counter() - start
            print(f"Correct, you´ve guessed the"
            f"right number in {attempts} guesses!")
            print(f"It tooks {elapsed:.2f} seconds.")
            break
        
        else:
            attempts += 1
            used_numbers.add(player_nr)
            result = bulls_cows_counter(player_nr,secret_number)
                
            plur = inflect.engine()
            word_1 = "bull"
            word_2 = "cow"

            print(f"{result[0]} {plur.plural(word_1,result[0])}," 
                  f"{result[1]} {plur.plural(word_2,result[1])}")


if __name__ == "__main__":
    main_game()


        
  
        

