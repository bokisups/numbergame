import random
import json

name = input("ENTER YOUR NAME: ")

# GAME FUNCTION - kot argument vnesemo: mode = "easy" ali "hard" ter range = "poljubno število, npr. 20"
# S tem se znebimo potrebe po dveh ločenih funkcijah

def play_game(mode, range):
   
    secret = random.randint(1, range)
    attempts = 0
    failed_attempts = 0

    best_score = get_score_list()

    while True:
        guess = int(input(f"Guess the number between 1 and {range}: "))

        attempts += 1

        if guess == secret:
            best_score.append({"attempts" : attempts, "name": name, "failed": failed_attempts, "difficulty": mode})

            with open("records1.json","w") as reserv_file:
                reserv_file.write(json.dumps(best_score))

            print(f"Bravo, it is {secret}")
            print(f"You did it in {attempts} attempts")
            break

        elif guess > secret and mode == "easy":
            print("Try smaller ...")
            failed_attempts += 1

        elif guess < secret and mode == "easy":
            print("Try larger ...")
            failed_attempts += 1

# RECORDS
def get_score_list():
    with open("records1.json", "r") as reserv_file:
        best_score = json.loads(reserv_file.read())
        return best_score

# GAME LOOP
while True:

    selection = input("A) Play game B) See the best scores C) Press any key to QUIT ")

    if selection == "A" or selection== "a":

        mode = input("Choose your difficulty: Hard or Easy. ")

        if mode == "Hard" or mode == "hard":
            play_game(mode="hard", range=40)

        elif mode == "Easy" or mode == "easy":
            play_game(mode="easy", range=20)

    elif selection == "B" or selection == "b":
        for dict in get_score_list():           
           print(f"Player: {dict["name"]}, won in {dict["attempts"]} attempts. Failed {dict["failed"]} times. Mode: {dict["difficulty"]}")

    else:
            break
    
    #Domen - korekcija