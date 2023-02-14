from InsertUserData import insertInfo
from checkUserData import checkUniqueMail
from checkUserData import checkUniqueUsertId
import re
mailRegex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phoneRegex = r'^01[0125][0-9]{8}$'


def Register():
    print(" REGISTER \n")
    userId = input("Enter your user ID: ")
    while True:
        if userId.isnumeric():
            if checkUniqueUsertId(userId):
                break
        else:
            userId = input("invalid field, please enter your user ID: ")

    fName = input("Enter your first name: ")
    while True:
        if fName.isalpha():
            break
        else:
            fName = input("invalid field, re-enter your first name: ")

    lName = input("Enter your last name: ")
    while True:
        if lName.isalpha():
            break
        else:
            lName = input("invalid field,re-enter your last name: ")

    usrMail = input("Enter ur email: ")
    while True:
        if usrMail:
            if (re.fullmatch(mailRegex, usrMail)):
                if checkUniqueMail(usrMail):
                    break
            else:
                print("Invalid Email")
                usrMail = input("re-enter a valid email: ")
            break
        else:
            usrMail = input("Empty field, re-enter your email: ")
    usrPass = input("Enter a password: ")
    while True:
        if usrPass:
            break
        else:
            usrPass = input("Empty field,re-enter your password: ")

    usrPass2 = input("please re-enter the password: ")
    while True:
        if usrPass2:
            if usrPass2 == usrPass:
                break
            else:
                print("password doesn't match")
                usrPass2 = input("please re-enter the password: ")
            break
        else:
            usrPass2 = input("Empty field, please re-enter your password: ")

    usrPhone = input("Enter your phone number: ")
    while True:
        if usrPhone:
            if (re.fullmatch(phoneRegex, usrPhone)):
                break
            else:
                print("Invalid phone")
                usrPhone = input("please enter a valid phone number: ")
            break
        else:
            usrPhone = input("Empty field, please enter your phone: ")
    info = [userId, fName, lName, usrMail, usrPass, usrPhone]
    user_info = ":".join(info)
    insertInfo(user_info)
