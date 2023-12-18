import random
import json
import datetime
from heapq import nlargest


name = input("Name ")

def play_game():


    secret = random.randint(1, 30)

    

    attempts = 0
    failed_attempts = 0
    best_score = get_score_list()
    while True:
        guess = int(input("Guess the num 1 to 30 "))

        attempts += 1
        failed_attempts = attempts - 1

        if guess == secret:
            best_score.append(
            {"attempts" : attempts,
                "date": str(datetime.datetime.now()),
                "name":name, "failed":failed_attempts})

            with open("records.json","w") as reserv_file:
                reserv_file.write(json.dumps(best_score))

            print("Bravo its",(secret))
            print(f"You did it in {attempts} attempt")
            break
        elif guess > secret:
            print("Try smaller then",(guess))
        elif guess < secret:
            print("Try larger then",(guess))


    



def get_score_list():
    with open("records.json", "r") as reserv_file:
        best_score = json.loads(reserv_file.read())
        return best_score


while True:
    selection = input("A) Play game? B) See the best scores? Press any to - Quit?")
    if selection == "A" or selection== "a":
        play_game()
    elif selection == "B" or selection == "b":
        for dict in get_score_list():           
           print(f"Player: {dict["name"]},won in {dict["attempts"]} attempts. Failed {dict["failed"]} times.")
    else:
            break

           

            
       


     
          