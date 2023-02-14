def checkData(userMail, password):
    with open("Users.txt") as rfile:
        users = rfile.readlines()
        for user in users:
            user_info = user.split(":")
            if user_info[3] == userMail and user_info[4] == password:
                return True
    return False


def checkUniqueMail(registerMail):
    with open("Users.txt") as rfile:
        users = rfile.readlines()
        for user in users:
            user_info = user.split(":")
            if user_info[3] == registerMail:
                print("repeated mail")
                exit()
    return True


def checkUniqueProjectId(projectId):
    with open("Projects.txt") as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            if proj_info[0] == projectId:
                print("repeated project id")
                exit()
    return True


def checkUniqueUsertId(userId):
    with open("Users.txt") as rfile:
        users = s = rfile.readlines()
        for user in users:
            user_info = user.split(":")
            if user_info[0] == userId:
                print("repeated user id")
                exit()
    return True
