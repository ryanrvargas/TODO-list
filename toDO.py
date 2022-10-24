import os
import datetime

date = str(datetime.datetime.now())
time = str(datetime.datetime.now())
date= date[:10]
time = time[12:16]

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
            getTaskSize()
            print("Good Bye")
            return True
        case _:
            print("Inproper input, selection from the options")

####Get task from user
def getTask():
    global list
    num, x= 0, 0
    running = True
    print("How many Task are in your list")

    #Make sure user inputs a integer
    while running:
        num = input()
        if num == int or num == "" or num != 0 or (x+1) == num:
            for x in range(int(num)):
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

#Removing task from 
def removeTask():
    word = input("What task would you like to remove ")
    word = word.lower()
    
    with open(username + ".txt", "r") as inputs:
        with open("temp.txt", "w") as output:
            for line in inputs:
                if not line.strip("\n").startswith(word):
                    output.write(line)

    os.replace('temp.txt', username + '.txt')
    

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
        listSize += 1
    f.close()
    print(str(listSize) + " things in list")
     
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
    print("\nDate " + date + " Time " + time)
    print("Welcome to you To-Do list " + username + ".\n-To add to your list type 'add'\n-To remove" 
                + " type 'remove' \n-To view list type 'list'\n-To change user type 'change " 
                + "user'\n-To stop type 'stop'\n")
        


if __name__ == '__main__':
    main()
    

#os.system("git add toDO.py")
#os.system("git commit -m 'get size of to do list, prints when stopped'")
#os.system("git push")


