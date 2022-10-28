#https://github.com/ryanrvargas
import os
import datetime
from rich import print
from rich.console import Console
from rich.style import Style
console = Console()

date = str(datetime.datetime.now())
time = str(datetime.datetime.now())
date= date[:10]
time = time[12:16]
uses = 0

error_code = Style(color="red", blink=True, bold=True)
prompt = Style(color = "white", bold=True)

def main():
    global date,time

    exit = False 
    getUser()   
    
    while not exit:
        date = str(datetime.datetime.now())
        time = str(datetime.datetime.now())
        date= date[:10]
        time = time[12:16]
        getList()
        TUI()
        exit = options()
    
def options():
    word = input()
    match word.lower():
        case "add":
            getTask()
        case "remove":
            words = input("What task would you like to remove ")
            removeTask(words)
        case "change":
            getUser()
        case "completed":
            completed()
        case "stop":
            getTaskSize()
            print("Good Bye")
            return True
        case _:
            print("Inproper input, selection from the options")

def completed():
    global uses
    console.print("Enter amount of task completed ", style = prompt)
    num = input()
    if num.isdigit():
        #if uses is less than 1 it'll print complete task once
        if uses < 1:
            with open(username + ".txt", "a") as f:
                f.write("completed task" + "\n")
        uses += 1
        for x in range(int(num)):
            print("Enter task: ")
            words = input()
            words = words.lower()
            removeTask(words) 
            with open(username + ".txt", "a") as f:
                f.write(words + "\n")
    else:
        console.print("Input a number(Digit)", style = error_code)
        
#Get task from user
def getTask():
    num, x= 0, 0
    running = True
    completed = False
    console.print("How many task would you like to add to your list?", style = prompt)
    
    #Determine weather there are completed task in file of user
    with open(username + ".txt", "rt") as f:
        list = f.readlines()
    for x in list:
        if x.strip() == "completed task":
            completed = True
    
    while running:
        num = input()
        if num.isdigit() and completed == False:
            n = int(num)
            for x in range(n):
                word = input("Task: ")
                word = word.lower()
                with open(username + ".txt", "a") as f:
                    f.write(word + "\n")
                if (x+1) == int(num):
                    f.close()
                    running = False
                    break
        elif num.isdigit() and completed == True:
            num = int(num)
            addTaskC(num)
            break
        else:
            console.print("Invalid input, try inputting a number", style = error_code)
#This function adds new task before the completed task but still go at the bottom of the list instead of push the older task to the bottom       
def addTaskC(tAmount):
    storage = []
    number= 0
    completed = False
    with open(username + ".txt", "rt") as f:
        list = f.readlines()
    #Find out if "completed task" is in the list.
    for x in list:
        if x.strip() == "completed task":
            completed = True
        #Start storing completed task in an array then remove them from list
        if completed == True:
            storage.append(x)
            #print(storage[number], end = "")
            removeTask(storage[number].strip())
            number += 1
    #Input new task 
    for x in range(tAmount):
        print("Task: ")
        word = input().lower()
        with open(username + ".txt", "a") as f:
            f.write(word + "\n")
    number = 0
    #Paste completed task at end of list
    for x in range(len(storage)):
        with open(username + ".txt", "a") as f:
            f.write(storage[number].strip() + "\n")
        number += 1

#Removing task from 
def removeTask(word):
    word = word.lower()
    with open(username + ".txt", "r") as inputs:
        with open("temp.txt", "w") as output:
            for line in inputs:
                if not line.strip("\n").startswith(word):
                    output.write(line)

    os.replace('temp.txt', username + '.txt')
    
#Print task user has inputted
def getList():
    num, numAtTrue, count, page = 0, 0, 0, 1
    crossWord = False
    console.print("-----Current List-----", style = "bold italic")
    console.print("Page " + str(page), style = "bold white")
    with open(username + ".txt", "rt") as f:
        list = f.readlines()
    #Print out all the words in the toDo.txt list file
    for x in list:
        count += 1
        num += 1
        #Find Completed Task
        if x.strip() == "completed task":
            crossWord = True
            numAtTrue = num + 1
        #If Completed Task is found, and num is greater than numAtTrue then put a strike through the word
        if num >= numAtTrue and crossWord == True:
            print(str(num) + " ", end = "")
            console.print(x, end = "", style = "strike")
        else:
            print(str(num) + " "+ x, end = "")
        if count >= 15:
            page += 1
            count = 0
            console.print("Page " + str(page), style = "bold white")
        
    f.close()

#Print amount of task
def getTaskSize():
    global listSize
    listSize = -1
    with open(username + ".txt", "rt") as f:
        list = f.readlines()
    for x in list:
        listSize += 1
    f.close()
    if listSize < 0:
        listSize = 0
    print(str(listSize) + " things in list")

def getUser():
    global username
    username = ""
    while username == "":
        console.print("Input username: ", style = "red bold")
        username = input()
        if username == "":
            print("Characters are required for username, use anything \nTry again ")
        else:
            console.print("Hello " + username, style = "italic")
            f = open(username + ".txt", "a")
            f.close()

def TUI():
    print("\nDate " + date + " Time " + time)
    console.print("[not bold]Welcome to your To-Do list[/not bold] " + username + ".\n-To add to your list type 'add'\n-To remove" 
                + " type 'remove'\n-To change user type 'change'\n-To make a completed task type 'completed' "
                + "user'\n-To stop type 'stop'\n", style = prompt)
        
if __name__ == '__main__':
    main()

os.system("git add toDO.py")
os.system("git commit -m 'list size is fix'")
os.system("git push")
"""
WANTS
-1Printing list is default behavior(GOOD)
2No more than 15 items should be printed at once
(Split into pages) Each page with 15 items max
3Save completed task(Good)
4Show completed task(words should have a different color or line
in between to tell the difference between complete and non completed(GOOD)
5Completed task at begin of list should be deleted(HUH?)
First task in list should always be incomplete(GOOD)
List should always be in front of person before they are asked to do anything(GOOD)

"""
