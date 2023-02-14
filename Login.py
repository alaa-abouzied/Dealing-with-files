from checkUserData import checkData
from ProjectMenu import projectMenu


def Login():
    print(" LOGIN ")
    usrMail = input("please enter your email: ")
    while True:
        if usrMail:
            break
        else:
            usrMail = input("Empty field, Enter your email: ")

    usrPass = input("Enter your password: ")
    while True:
        if usrPass:
            break
        else:
            usrPass = input("Empty field, Enter your password: ")

    if checkData(usrMail, usrPass):
        print("logged in successfully")
        return projectMenu(usrMail)
    print("Error: enter correct data")
    return Login()
