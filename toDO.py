list = []

user = input("How many Task are in your list ")

####get task from user
for x in range(int(user)):
    user = input("Task:" + str(x + 1) + " ")
    list += [user] #makes list array size

####output tasks from user
for x in range(len(list)):
    print(list[x])
