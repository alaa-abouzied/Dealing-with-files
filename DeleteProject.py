def deleteProject(usrMail):
    print(" DELETE PROJECT ")
    print("All projects:\n")
    newList = []
    with open("Projects.txt", "r") as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            newList.append(proj_info)
            print(proj_info[1])
            if proj_info[0] == usrMail:
                print(proj_info)
            else:
                print("not the owner user")
    myProjID = input("enter id of project u want to delete: ")
    if myProjID.isnumeric():
        for pos, i in enumerate(newList):
            print(pos, i)
            print(i[0])
            if i[0] == myProjID:
                newList[pos].clear()
                print(newList[pos])
                with open("Projects.txt", "w") as pfile:
                    with open("Projects.txt", "a") as pfile:
                        for i in newList:
                            pfile.write(":".join(i))

    else:
        myProj = input("invalid field, please enter ur project ID: ")

    return True
