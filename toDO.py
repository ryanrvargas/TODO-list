list = []

user = input("How many Task are in your list ")

for x in range(int(user)):
    user = input("Task:" + str(x + 1) + " ")
    list += [user]
    
for x in range(len(list)):
    print(list[x])
