list = [""]

####get task from user
def getTask(task):
    global list
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
        list[x] = task[x]
        
    
    
####removing task from 
def removeTask():
    word = input("What task would you like to remove ")
    """
    for x in range(len(list)):
        if word.lower() == list[x]:
            list[x] = ""
            """

####output tasks from user
def printTask():
    print("-----Current Task-----")
    for x in range(len(list)):
        print(list[x])

####get task from user
getTask(list)
printTask()
removeTask()
printTask()
    
