import os
import datetime

list = [""]
taskAmount = 0
run = True


def main():
    exit = False
    
    getUser()
    TUI()
    
    while not exit:
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
        case "stop":
            print("Good Bye")
            return True
    
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
                word = input("Task:" + str(x + 1) + " ")
                word = word.lower()
                task += [word] #makes list array size
                f = open(username + ".txt", "a")
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
    list.remove(word)
    
    f = open(username + ".txt", "rt")
    data = f.read()
    data = data.replace(word, "")
    f.close
    f = open(username + ".txt", "wt")
    f.write(data)
    f.close()

    taskAmount -= 1

####Print task user has inputted
def getList():
    print("-----Current Task-----")
    f = open(username + ".txt", "rt")
    list = f.readlines()
    for x in list:
        print(x, end = "")
    f.close()
    
    
####Print amount of task
def getTaskSize():
    print("Total number of task are :" + str(taskAmount))
    
def getUser():
    global username
    username = input("Input username: ")
    while username == "":
        name = input("Characters are required for username, use anything \nTry again\nInput Username: ")
        if name == "":
            print("Characters are required for username, use anything \nTry again\nInput Username: ")
        else:
            print("Hello " + username)
            run = False

def TUI():
    print("Welcome to you To-Do list.\n-To add to your list type 'add'\n-To remove" 
                + " type 'remove' \n-To view list type 'list'\n-To change user type 'change " 
                + "user'\n-To stop type 'stop'\n")
    
    
ct = datetime.datetime.now()
print(ct)


if __name__ == '__main__':
    main()
   
os.system("git add toDO.py")
os.system("git commit -m 'Now able to get user, add text to file and remove from file '")
os.system("git push")


