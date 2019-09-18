import os
import json
import datetime
date = datetime.datetime.today()
cls = lambda: os.system('cls')

accNmbDict = {}

def TransJsonLoad():
    with open("transaktioner.txt") as json_file:
        accNmbDict = json.load(json_file)

def TransJsonSave():
    with open("Transactions.txt", "a+") as json_file:
        json.dump(accNmbDict,json_file)

def CheckIfInt():
    while True:
        try:
            methodInput = int(input())
            return methodInput
        except:
            print("Invalid input, try again")

def CreateAcc():
    cls()
    print("------Create Account-----")
    while True:
        print("Enter desired account number: ")
        createAccNmb = CheckIfInt()
        if createAccNmb in accNmbDict:
            print("This account number is not available")
        else:
            accNmbDict[createAccNmb] = 0
            TransJsonSave()
            print(f"Your account wih account number {createAccNmb} has been created")
            input("Press Enter to continue")
            return accNmbDict
def LogIn():
    cls()
    print("-----Log in------")
    print("Enter account number: ")
    logInAccNmb = CheckIfInt()
    if logInAccNmb in accNmbDict:
        AdminAccMenu(logInAccNmb)
    else:
        print("That account number does not exist.")
        input("Press Enter to continue")

def Deposit(logInAccNmb):
    cls()
    print("------Deposit------")
    print("Enter the desired amount to deposit")
    depositInput = CheckIfInt()
    if depositInput < 0:
        print("The amount entered is too low")
        print("Press Enter to continue")
    else:
        accNmbDict[logInAccNmb] += depositInput
        TransJsonSave()
        print(f"{depositInput} has been deposited to your account")
        input("Press Enter to return")
        return depositInput

def ShowBalance(logInAccNmb):
    cls()
    print("-------Balance------")
    balance = accNmbDict[logInAccNmb]
    print(f"Account balance: {balance}")
    input("Press Enter to return")

def Withdraw(logInAccNmb):
    cls()
    print("-------Withdraw------")
    print("Enter the desired amount to withdraw")
    withdrawInput = CheckIfInt()
    if withdrawInput > accNmbDict[logInAccNmb]:
        print("The amount exceeds the balance of your account")
        input("Press Enter to continue")
    else:
        accNmbDict[logInAccNmb] -= withdrawInput
        TransJsonSave()
        print(f"{withdrawInput} has been withdrawn from your account")
        input("Press Enter to return")

def AdminAccMenu(logInAccNmb):
    while True:
        cls()
        print(f"-----ADMINISTER ACCOUNT----- ACCNR: {logInAccNmb}")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Show balance")
        print("4. Log out")
        
        selec = CheckIfInt()

        if selec == 1:
            Withdraw(logInAccNmb)
        elif selec == 2:
            Deposit(logInAccNmb)
        elif selec == 3:
            ShowBalance(logInAccNmb)
        elif selec == 4:
            break
        else:
            print("Invalid input, try again")
            input("Press Enter to return")

while True:
    cls()
    print("----MAIN MENU----")
    print("1. Create account")
    print("2. Log in")
    print("3. Exit")
    
    selec = CheckIfInt()

    if selec == 1:
        CreateAcc()

    elif selec == 2:
        LogIn()

    elif selec == 3:
        break
    else:
        print("Invalid input, try again")
        input("Press Enter to continue")
        cls