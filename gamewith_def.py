import random
import json



name = input("Name ")

    
def level_easy(): # E A S Y .................. M O D E
   
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
                #"level": mode,
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

def level_hard():# H A R D .....................  M O D E

    secret = random.randint(1, 40)
    attempts = 0
    failed_attempts = 0
    best_score = get_score_list()
    
    while True:
        guess = int(input("Guess the num 1 to 40 "))

        attempts += 1
        failed_attempts = attempts - 1

        if guess == secret:
            best_score.append(
            {"attempts" : attempts,
                #"level": mode,
                "name":name, "failed":failed_attempts})

            with open("records.json","w") as reserv_file:
                reserv_file.write(json.dumps(best_score))

            print("Bravo its",(secret))
            print(f"You did it in {attempts} attempt")
            break
        elif secret > 20:
            print("No its not.  Hint: 20+. Try again.")
        elif secret < 20:
            print("No its not.  Hint: 20-. Try again.")


def get_score_list():
    with open("records.json", "r") as reserv_file:
        best_score = json.loads(reserv_file.read())
        return best_score

while True:

    selection = input("A) Play game? B) See the best scores? Press any to - Quit? ")
    if selection == "A" or selection== "a":
        mode = input("Chose your level. Hard or Easy ")
        if mode == "Hard" or mode == "hard":
            level_hard()
        elif mode == "Easy" or mode == "easy":
            level_easy()
    elif selection == "B" or selection == "b":
        for dict in get_score_list():           
           print(f"Player: {dict["name"]},won in {dict["attempts"]} attempts. Failed {dict["failed"]} times.")
    else:
            break