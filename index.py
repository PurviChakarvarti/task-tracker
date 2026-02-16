from datetime import datetime
import re #built in module for regex(used for validation)
import time

numPosPattern = "^[1-9]\\d*$" # start regex with '^' and end with '$'

def addTask():
    id = input("Enter id: \n> ") #\n for better input readability
    if not(re.match(numPosPattern , id)):
        print("Invalid input!")
        return  # use return to finish fxn by returning a value. 
    
    while True: # to take this particular input repeatedly rather than exiting fxn and starting again
        desc = input("Enter task description: \n> ")
        if re.match("^.{0}$", desc):
            print("Description cannot be blank!")
            continue
        elif not(re.match("^.{1,100}$", desc)) :
            print("Max 100 chars allowed!")
            continue 
        else:
            break  # above conds false, input true, move next

    status = "To Do"

    createdAt = datetime.now()
    updatedAt = datetime.now()

    print("Task Added Succesfully!")
    
print(f""" 
/ )( \(  __)(  )   / __)/  \ ( \/ )(  __)  (_  _)/  \   (_  _)/ _\ / ___)(  / )  (_  _)(  _ \ / _\  / __)(  / )(  __)(  _ \
\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _)     )( (  O )    )( /    \\___ \ )  (     )(   )   //    \( (__  )  (  ) _)  )   /
(_/\_)(____)\____/ \___)\__/ \_)(_/(____)   (__) \__/    (__)\_/\_/(____/(__\_)   (__) (__\_)\_/\_/ \___)(__\_)(____)(__\_)\n\n""")   
#formatting               
while True:
    print("1. Add a Task")
    print("2. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            addTask()
        case "2":
            print("Exiting..")
            time.sleep(2)  # wait for 2 secs
            break
        case "": # empty choice not allowed
            print("invalid input!")
        case _:
            print("invalid input!")  #no spaces allowed

