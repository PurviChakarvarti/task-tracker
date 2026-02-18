from datetime import datetime
import re #built in module for regex(used for validation)
import time
import json

numPosPattern = "^[1-9]\\d*$" # start regex with '^' and end with '$'

def addTask():
    try:
        with open('tasks.json' , 'r') as file:  # read the whole json data in the variable to store it
            data_lst=json.load(file)
    except FileNotFoundError:      # if no json file, then create an empty list to transfer to json
        data_lst=[]

    id = 0
    max_id=0

    if len(data_lst)!=0:
        for tasks in data_lst:
            id= tasks.get("id")
            max_id=max(id, max_id)
            
    id = max_id + 1

    
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

    data = { # dictionary datatype to store vals in jsonfile
        "id" : id,
        "description" : desc,
        "status" : status,
        "createdAt" : createdAt.strftime("%d-%m-%Y, %H:%M:%S"),
        "updatedAt" : updatedAt.strftime("%d-%m-%Y, %H:%M:%S")
    }

    data_lst.append(data)

    with open('tasks.json', 'w') as file:  # open file as write so that json file truncates and we can put new data from variable with old data
        json.dump(data_lst, file, indent=2)

    print("Task Added Succesfully! with ID: ", id)

def updateTask():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    if len(data_lst) == 0:
        return print("No tasks found!")

    while True:
        id_input = input("Enter Task ID for updation: \n> ")
        if re.match("^.{0}$", id_input):
            print("ID cannot be blank!")
            continue
        elif not(re.match(numPosPattern,id_input)) :
            print("Wrong Input!")
            continue 
        else:
            break
        
    for tasks in data_lst:
        if int(id_input) == tasks.get("id"):
            newDescription = input("New description for task " + tasks.get("description") + " and ID " + id_input + "\n> ")
            newUpdatedAt = datetime.now()
            tasks['description'] = newDescription
            tasks['updatedAt'] = newUpdatedAt.strftime("%d/%m/%Y, %H:%M:%S")
            break
    else:
        return print("No Such ID Found.")
        
    with open('tasks.json', 'w') as file:
        json.dump(data_lst, file, indent=2)    
    print("ID" + id_input + ":" + "Task " + newDescription)

def deleteTask():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    if len(data_lst) == 0:
        return print("No tasks found!")
    
    while True:
        id_input = input("Enter Task ID for deletion: \n> ")
        if re.match("^.{0}$", id_input):
            print("ID cannot be blank!")
            continue
        elif not(re.match(numPosPattern,id_input)) :
            print("Wrong Input!")
            continue 
        else:
            break
    
    for tasks in data_lst:
        if int(id_input)==tasks.get("id"):
            data_lst.remove(tasks)  
            break        
    else:           # use for-else loop so if for exhausts wo breaking, else runs
        return print("No such ID exists!")
        
    with open('tasks.json', 'w') as file:
        json.dump(data_lst, file, indent=2)    
    print("Task deleted Successfully\n")

def markProgress():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    if len(data_lst) == 0:
        return print("No tasks found!")

    while True:
        id_input = input("Enter Task ID to change Status: \n> ")
        if re.match("^.{0}$", id_input):
            print("ID cannot be blank!")
            continue
        elif not(re.match(numPosPattern,id_input)) :
            print("Wrong Input!")
            continue 
        else:
            break
        
    for tasks in data_lst:
        if int(id_input) == tasks.get("id"):
            newUpdatedAt = datetime.now()
            tasks['status'] = "In-Progress"
            tasks['updatedAt'] = newUpdatedAt.strftime("%d/%m/%Y, %H:%M:%S")
            break
    else:
        return print("No Such ID Found.")
        
    with open('tasks.json', 'w') as file:
        json.dump(data_lst, file, indent=2)    
    print("ID" + id_input + ": Marked as 'In Progress'")
    

def markDone():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    if len(data_lst) == 0:
        return print("No tasks found!")

    while True:
        id_input = input("Enter Task ID to change Status: \n> ")
        if re.match("^.{0}$", id_input):
            print("ID cannot be blank!")
            continue
        elif not(re.match(numPosPattern,id_input)) :
            print("Wrong Input!")
            continue 
        else:
            break
        
    for tasks in data_lst:
        if int(id_input) == tasks.get("id"):
            newUpdatedAt = datetime.now()
            tasks['status'] = "Done"
            tasks['updatedAt'] = newUpdatedAt.strftime("%d/%m/%Y, %H:%M:%S")
            break
    else:
        return print("No Such ID Found.")
        
    with open('tasks.json', 'w') as file:
        json.dump(data_lst, file, indent=2)    
    print("ID" + id_input + ": Marked as 'Done'")

def listall():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    if len(data_lst) == 0:
        return print("No tasks found!")
    
    for tasks in data_lst:
        print(tasks)
    
def viewDone():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    
    if len(data_lst) == 0:
        return print("No tasks found!")
    
    for tasks in data_lst:
        if tasks.get("status")=="Done":
            print(tasks)

def viewProgress():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    if len(data_lst) == 0:
        return print("No tasks found!")
        
    for tasks in data_lst:
        if tasks.get("status")=="In-Progress":
            print(tasks)
   
def viewtodo():
    try:
        with open('tasks.json' , 'r') as file:      
            data_lst=json.load(file)
    except FileNotFoundError:       
        return print("Add a task first!") 
    if len(data_lst) == 0:
        return print("No tasks found!")
        
    for tasks in data_lst:
        if tasks.get("status")=="To Do":
            print(tasks)

def viewStatus():
    print("1. View 'Done' tasks")
    print("2. View 'In-Progress' tasks")
    print("3. View Tasks 'To-Do'")
    ch = input("Choose Tasks to view: \n")
    match ch:
        case "1":
            viewDone()
        case "2":
            viewProgress()
        case "3":
            viewtodo()
        case "": # empty choice not allowed
            print("invalid input!")
        case _:
            print("invalid input!") 

# print(f""" 
# / )( \(  __)(  )   / __)/  \ ( \/ )(  __)  (_  _)/  \   (_  _)/ _\ / ___)(  / )  (_  _)(  _ \ / _\  / __)(  / )(  __)(  _ \
# \ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _)     )( (  O )    )( /    \\___ \ )  (     )(   )   //    \( (__  )  (  ) _)  )   /
# (_/\_)(____)\____/ \___)\__/ \_)(_/(____)   (__) \__/    (__)\_/\_/(____/(__\_)   (__) (__\_)\_/\_/ \___)(__\_)(____)(__\_)\n\n""")   
# #formatting   
    
while True:
    print("1. Add a Task")
    print("2. Update Task")
    print("3. Delete Task")
    print("4. Mark as In-Progress")
    print("5. Mark as Done")
    print("6. View all tasks")
    print("7. View by Status")
    print("8. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case "1":
            addTask()
        case "2":
            updateTask()
        case "3":
            deleteTask()
        case "4":
            markProgress()
        case "5":
            markDone()
        case "6":
            listall()
        case "7":
            viewStatus()
        case "8":
            print("Exiting..")
            time.sleep(2)  # wait for 2 secs
            break
        case "": # empty choice not allowed
            print("invalid input!")
        case _:
            print("invalid input!")  #no spaces allowed
