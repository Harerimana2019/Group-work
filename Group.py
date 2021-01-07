def Menu():
    print("Welcome to MINEMA Online Support Center")
    print("1. Continue")
    print("2. Cancel")

def Continue_menu():
    print("Continue to MINEMA Online Support Center")
    print("1. Identifications")
    print("2. Go Back")

def Cancel():
    print("Your request has been canceled")

def Identifications_menu():
    print("Identification Documents")
    print("1 Refugee ID")
    print("2 Passport")
    print("3 Go Back")

def ID_menu():
    print("Refugee ID")
    print("1. New ID")
    print("2. Update")
    print("3. Go Back")
def New_ID():
    print("1.Your Name")
    print("2. Go back")

def unknown_input(message):
    print("Your Request has been canceled")
def name():
    print("Enter Your Legal Names or 0 to go Back")
    print("1. Name")
    print("2. Go Back")

def PoR():
    print("Enter the Number of Your Proof of Registration or 0 to go Back")
    print("1.Proof of Registration")
    print("2. Go Back")

def message():
    print("Thank you for using MINEMA Online Support center. You have been registered to get a NEW ID, Please reach out to MIDMAR office for the next step")

def passport_menu ():
    print("Enter Your Name to register for Passport")
    print("1.You Name")
    print("2. Go Back")
def wrong_selection():
    print ("UNKOWN APPLICATION")
Menu()
input1 = int(input()) 
if input1 == 1:
    Continue_menu()
elif input1 == 2:
    Cancel()
else:
    wrong_selection()
input2 = int(input())
if input2 == 1:
    Identifications_menu()
elif input2 == 2:
    Menu()
input3 = int(input())
if input3 == 1:
    ID_menu()
elif input3 == 2:
    passport_menu()
elif input3 == 3:
    Continue_menu()
else:
    wrong_selection()
input4 = int(input())
if input4 == 1:
    name()
input5 = input()
PoR()
input6 = input()
message()
