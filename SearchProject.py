def searchProjects():
    print(" search PROJECT ")
    print("All Projects:\n")
    newList = []
    projectStartDate = input("enter start date of project you want to view: ")
    projectStartDate
    with open("Projects.txt", "r") as pfile:
        projects = pfile.readlines()
        for proj in projects:
            proj_info = proj.split(":")
            newList.append(proj_info)
            if proj_info[5] == projectStartDate:
                print(proj_info)
            else:
                print("not valid date")
