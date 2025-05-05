"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jan Kuděla
email: jochanan.jorgen@gmail.com
"""

import random
import inflect

def secret_number_gen():
    secret_number = str(random.randint(1000,9999))
    return secret_number

secret_number = secret_number_gen()
#print(secret_number)
print("Hi there!")
line = 45 * "-"
print(line)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")

player_number = str()
attemppts = 0
used_numbers = set()

while secret_number != player_number:
    print(line)
    player_number = (input("Enter a number: "))

    if player_number == secret_number:
        print(f"Correct, you´ve guessed the right number in {attemppts} guesses!")
        break
    if not player_number.isdigit():
        print("Your have to enter number.")
    elif len(player_number) != 4:
        print("Your number have to be 4 digit long.")
    elif player_number[0] == "0":
        print("Your number can´t begin with 0 .")
    elif player_number in used_numbers:
        print("You have already used this number.")
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
            
        p = inflect.engine()
        word_1 = "bull"
        word_2 = "cow"

        print(f"{bulls} {p.plural(word_1,bulls)}, {cows} {p.plural(word_2,cows)}")
        
  
        

    

