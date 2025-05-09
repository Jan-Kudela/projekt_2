"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgen@gmail.com
"""

import random
import inflect
import time

def secret_number_gen():
    secret_num = random.sample(range(10), 4)
    if secret_num[0] == 0:
        for num in range(1, 4):
            if secret_num[num] != 0:
                secret_num[0], secret_num[num] = secret_num[num], secret_num[0]
                break
    
    secret_num_complete = "".join(str(number) for number in secret_num)  
    return secret_num_complete

secret_number = secret_number_gen()
print(secret_number)

def line_printer():
    line = 45 * "-"
    print(line)

start = time.perf_counter()

print("Hi there!")
line_printer()

print(f"I've generated a random 4 digit number for you."
    f"\nLet's play a bulls and cows game.")


player_number = str()
attemppts = 1
used_numbers = set()

while secret_number != player_number:
    line_printer()
    player_number = (input("Enter a number: "))

    if player_number == secret_number:
        elapsed = time.perf_counter() - start
        print(f"Correct, you´ve guessed the"
        f"right number in {attemppts} guesses!")
        
        print(f"It took {elapsed:.2f} seconds.")
        break
    
    if not player_number.isdigit():
        print("Your have to enter number.")
    elif len(player_number) != 4:
        print("Your number have to be 4 digit long.")
    elif player_number[0] == "0":
        print("Your number can´t begin with 0 .")
    elif player_number in used_numbers:
        print("You have already used this number.")
    elif len(player_number) != len(set(player_number)):
        print("Your number contains duplicate digits.")
    else:
        attemppts += 1
        used_numbers.add(player_number)
        bulls = 0
        cows = 0
        for letter in range(4):
            
            if player_number[letter] == secret_number[letter]:
                bulls += 1
            elif player_number[letter] in secret_number:
                cows += 1
            
        plur = inflect.engine()
        word_1 = "bull"
        word_2 = "cow"

        print(f"{bulls} {plur.plural(word_1,bulls)}, {cows} {plur.plural(word_2,cows)}")
        
  
        

    

