import os
import datetime

list = [""]
taskAmount = 0
run = True


def main():
    exit = False 
    getUser()   
    
    while not exit:
        TUI()
        exit = options()
    
def options():
    word = input()
    match word.lower():
        case "add":
            getTask()
        case "remove":
            removeTask()
        case "list":
            getList()
        case "change user":
            getUser()
        case "stop":
            print("Good Bye")
            return True
        case _:
            print("Inproper input, selection from the options")

####Get task from user
def getTask():
    global list
    global taskAmount
    num, x= 0, 0
    task = []
    running = True
    print("How many Task are in your list")

    #Make sure user inputs a integer
    while running:
        num = input()
        if num == int or num == "" or num != 0 or (x+1) == num:
            for x in range(int(num)):
                taskAmount = int(num)
                word = input("Task: ")
                word = word.lower()
                task += [word] #makes list array size
                with open(username + ".txt", "a") as f:
                    f.write(word + "\n")
                if (x+1) == int(num):
                    f.close()
                    running = False
                    break
        else:
            print("Invalid input, try inputting a number")
    #Copy one array to another
    for x in range(len(task)):
        #print(x, end = " ")
        list += [task]
        list[x] = task[x].lower()

#Removing task from 
def removeTask():
    global taskAmount
    word = input("What task would you like to remove ")
    word = word.lower()
    #list.remove(word)
    
    with open(username + ".txt", "r") as inputs:
        with open("temp.txt", "w") as output:
            for line in inputs:
                if not line.strip("\n").startswith(word):
                    output.write(line)

    # replace file with original name
    os.replace('temp.txt', username + '.txt')
    
    taskAmount -= 1

####Print task user has inputted
def getList():

    print("-----Current List-----")
    with open(username + ".txt", "rt") as f:
        list = f.readlines()
    for x in list:
        print(x, end = "")
    f.close()
        
####Print amount of task
def getTaskSize():
    global listSize
    listSize = 0
    with open(username + ".txt", "rt") as f:
        list = f.readlines()
    for x in list:
        print(x, end = "")
        listSize += 1
    f.close()
    
    
def getUser():
    global username
    username = ""
    while username == "":
        username = input("Input username: ")
        if username == "":
            print("Characters are required for username, use anything \nTry again ")
        else:
            print("Hello " + username)
            f = open(username + ".txt", "a")
            f.close()

def TUI():
    print("\nWelcome to you To-Do list " + username + ".\n-To add to your list type 'add'\n-To remove" 
                + " type 'remove' \n-To view list type 'list'\n-To change user type 'change " 
                + "user'\n-To stop type 'stop'\n")
        
ct = datetime.datetime.now()
print(ct)

if __name__ == '__main__':
    main()

os.system("git add toDO.py")
os.system("git commit -m 'Now able to get user, add text to file and remove from file. New TUI '")
os.system("git push")



