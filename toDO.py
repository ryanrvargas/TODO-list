list = [""]
taskAmount = 0

####get task from user
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

    for x in range(len(task)):
        #print(x, end = " ")
        list += [task]
        list[x] = task[x].lower()
        taskAmount += 1

####removing task from 
def removeTask():
    global taskAmount
    word = input("What task would you like to remove ")
    word = word.lower()
    list.remove(word)
    taskAmount -= 1

####output tasks from user
def printTask():
    print("-----Current Task-----")
    for x in range(len(list)):
        print(list[x])
        
def taskSize():
    #for x in range(len(list)):
        #global taskAmount
        #taskAmount += 1
    print("Total number of task are :" + str(taskAmount))

####get task from user
getTask()
printTask()
removeTask()
printTask()
taskSize()
