import json
import random

def game():
    score = 0
    for i in range(5):
        operation = random.randint(1,4)
        if operation == 1:
            num1 = random.randint(1,1000)
            num2 = random.randint(1,1000)
            result = num1 + num2
            answer = int(input("What is the answer to " + str(num1) + " + " + str(num2) + "?"))
            if answer == result:
                score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        elif operation == 2:
            num1 = random.randint(1,1000)
            num2 = random.randint(1,1000)
            result = 0
            if num1 > num2:
                result = num1 - num2
                answer = int(input("What is the answer to " + str(num1) + " - " + str(num2) + "?"))
                if answer == result:
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            else:
                result = num2 - num1
                answer = int(input("What is the answer to " + str(num2) + " - " + str(num1) + "?"))
                if answer == result:
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
        elif operation == 4:
            num1 = random.randint(1,20)
            num2 = random.randint(1,20)
            result = num1 * num2
            answer = int(input("What is the answer to " + str(num1) + " * " + str(num2) + "?"))
            if answer == result:
                score += 1
                print("Correct!")
            else:
                print("Incorrect!")
        elif operation == 3:
            num1 = random.randint(1,1000)
            num2 = random.randint(1,40)
            if num1 % num2 == 0:
                result = num1 * num2
                answer = int(input("What is the answer to " + str(num1) + " / " + str(num2) + "?"))
                if answer == result:
                    score += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
    return score

def updateJson():
    with open("users.json", "w") as file:
        loaded_data.sort(key=myFunc, reverse=True)
        json.dump(loaded_data, file)

with open("users.json", "r") as json_file:
    loaded_data = json.load(json_file)
def myFunc(e):
    return e['score']

#print(loaded_data[0]['username'])
username = ""
password = ""
loggedIn = False
while not loggedIn:
    choice = input("1.Create account\n2.Login")
    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")
        for user in loaded_data:
            if user['username'] == username and user['password'] == password:
                loggedIn = True
                print("Logged in!")
    elif choice == "2":
        exists = False
        username = input("Username: ")
        password = input("Password: ")
        for user in loaded_data:
            if user['username'] == username:
                print("Account already exists")
                break
        loaded_data.append({'username' : username, 'password': password, 'score': 0})
        updateJson()
        loggedIn = True



while True:
    choice = int(input("1. Play game \n2. See top scores\n"))
    if choice == 1:
        score = game()
        for user in loaded_data:
            if user['username'] == username and user['password'] == password:
                user['score'] += score
                updateJson()
    elif choice == 2:
        print("Leaderboard")
        for i in range(len(loaded_data)):
            rank = i + 1
            #19 + name size
            titlebar = ""
            print("| " + str(rank) + ". " + loaded_data[i]['username'] + " with score: " + str(loaded_data[i]['score']) + " |")




            