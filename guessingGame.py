import random
import os
# úvodní věty
print("Vítejte ve hře Guess secret number. Porazte počítač.")
print("Tipněte si číslo od 1 do 100")

def guessing_game(start, end):
    # počet pokusů
    max_tries = input("Vyberte obtížnost. Napište 'easy' nebo 'hard': ")
    if max_tries == 'easy':
        max_tries = 10
    if max_tries == 'hard':
        max_tries = 5
    print(f"Počet pokusů je {max_tries}")

    number = random.randint(start, end) # generování náhodného čísla
    guess = None
    tries = 0
    
    # Hlavní kod hry
    while guess != number and tries < max_tries:
        guess = int(input(f"Tipněte si číslo mezi {start} a {end}: "))
        if guess < number:
            print("Příliš nízké!")
        elif guess > number:
            print("Příliš vysoke!")
        tries += 1
        print(f"zbýva {max_tries - tries} pokusů.")
    if guess == number:
        print("Gratulujeme! Uhádli jste správné číslo!")

    else:
        print(f"Počítač vyhrál. Prohrál jste. Hádané číslo bylo {number}.")

    # Vymazání obrazovky    
    new_game = input("Napište 'yes' pokud chcete ve hře pokračovat. 'no' pokud chctete hru ukončit. ")
    if new_game == "yes":
        os.system("cls")
        guessing_game(1, 100)
    else:
        os.system("cls")

guessing_game(1, 100)
