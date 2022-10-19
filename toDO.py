import os
import datetime

list = [""]
taskAmount = 0
run = True

def main():
    getTask()

####Get task from user
def getTask():
    global list
    global taskAmount
    task = []
    user = input("How many Task are in your list ")
    ####Make sure user inputs a integer
    try:
        for x in range(int(user)):
            user = input("Task:" + str(x + 1) + " ")
            task += [user] #makes list array size
        pass
    except ValueError:
        print("That was not an integer please try again")
        
    #copy one array to another
    for x in range(len(task)):
        #print(x, end = " ")
        list += [task]
        list[x] = task[x].lower()
        taskAmount += 1

####Removing task from 
def removeTask():
    global taskAmount
    word = input("What task would you like to remove ")
    word = word.lower()
    list.remove(word)
    taskAmount -= 1

####Print task user has inputted
def printTask():
    print("-----Current Task-----")
    for x in range(len(list)):
        print(list[x])
    taskSize()

####Print amount of task
def taskSize():
    print("Total number of task are :" + str(taskAmount))
    
ct = datetime.datetime.now()
print(ct)

def runPro():
    user = input("Welcome to you To-Do list to add to your list type 'add' to remove" 
                + " type 'remove' to view list type 'list' ")
    user = user.lower()

    try:
        if user == "add":
            ##print("You haven't created a list yet " + user.upper() + ". Will not work")
            getTask()
            while True:
                user = input("Input weather you'd like to add, remove, or view list. Or type 'stop' once you are done")
                match user:
                    case "add":
                        getTask()
                    case "remove":
                        removeTask()
                    case "list":
                        printTask()    
                    case "stop":
                      print("Good Bye")
                      #run = False
                      break
        elif user == "stop":
            print("Good Bye")
            run = False
        else:
            print("You don't have a list yet")
            run = False
                      
    except ValueError:
        print("That was not a proper input")
    
for x in range(20):
    print("-", end = " ")
print()    


if __name__ == '__main__':
    main()
    
os.system("git add toDO.py")
os.system("git commit -m 'Updates to toDO.py file'")
os.system("git push")

####TEST

