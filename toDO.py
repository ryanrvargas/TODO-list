list = [""]
taskAmount = 0

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

####Print amount of task
def taskSize():
    print("Total number of task are :" + str(taskAmount))

####TEST
getTask()
printTask()
removeTask()
printTask()
taskSize()
