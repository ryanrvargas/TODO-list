import os
import datetime
from rich import print
from rich.console import Console
console = Console()

date = str(datetime.datetime.now())
time = str(datetime.datetime.now())
date= date[:10]
time = time[12:16]
uses = 0

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
    print("[bold]Enter amount of task completed ")
    num = input()
    if num.isdigit():
        #if uses is less than 1 it'll print complete task once
        if uses < 1:
            with open(username + ".txt", "a") as f:
                f.write("Completed Task" + "\n")
        uses += 1
        print(uses)
        for x in range(int(num)):
            print("Enter task: ")
            words = input()
            words = words.lower()
            removeTask(words) 
            with open(username + ".txt", "a") as f:
                f.write(words + "\n")
    else:
        print("Input a number(Digit)")
        
####Get task from user
def getTask():
    global task
    task  = []
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
                task += word
                with open(username + ".txt", "a") as f:
                    f.write(word + "\n")
                if (x+1) == int(num):
                    f.close()
                    running = False
                    break
        else:
            print("Invalid input, try inputting a number")

#Removing task from 
def removeTask(word):
    word = word.lower()
    with open(username + ".txt", "r") as inputs:
        with open("temp.txt", "w") as output:
            for line in inputs:
                if not line.strip("\n").startswith(word):
                    output.write(line)

    os.replace('temp.txt', username + '.txt')
    

####Print task user has inputted
def getList():
    num, numAtTrue = 0, 0
    crossWord = False
    console.print("-----Current List-----", style = "bold italic")
    with open(username + ".txt", "rt") as f:
        list = f.readlines()
    for x in list:
        num += 1
        #Find Completed Task
        if x.strip() == "Completed Task":
            crossWord = True
            numAtTrue = num + 1
        #If Completed Task is found, and num is greater than numAtTrue then put a strike through the word
        if num >= numAtTrue and crossWord == True:
            print(str(num) + " ", end = "")
            console.print(x, end = "", style = "strike")
        else:
            print(str(num) + " "+ x, end = "")
    print(crossWord)
    print(numAtTrue)
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
        console.print("Input username: ", style = "color(1) bold")
        username = input()
        if username == "":
            print("Characters are required for username, use anything \nTry again ")
        else:
            print("Hello " + username)
            f = open(username + ".txt", "a")
            f.close()

def TUI():
    print("\nDate " + date + " Time " + time)
    print("Welcome to you To-Do list " + username + ".\n-To add to your list type 'add'\n-To remove" 
                + " type 'remove'\n-To change user type 'change'\n-To make a completed task type 'completed' "
                + "user'\n-To stop type 'stop'\n")
        
if __name__ == '__main__':
    main()

os.system("git add toDO.py")
os.system("git commit -m 'Cross line going across completed task.'")
os.system("git push")
"""
WANTS
-1Printing list is default behavior(GOOD)
2No more than 15 items should be printed at once
(Split into pages) Each page with 15 items max
3Save completed task(Good)
4Show completed task(words should have a different color or line
in between to tell the difference between complete and non completed
5Completed task at begin of list should be deleted(HUH?)
First task in list should always be incomplete(GOOD)
List should always be in front of person before they are asked to do anything(GOOD)

"""
