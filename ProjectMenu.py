from addProject import addProject
from ViewAllProjects import viewProjects
from EditProject import editProject
from DeleteProject import deleteProject
from SearchProject import searchProjects


def projectMenu(usrMail):
    y = input(
        "please choose one of the following options\n"
        "'a' for adding a new project\n'v' for viewing all projects\n"
        "'e' for editing a project\n'd' for deleting a project : \n""'s' for search for projects by start date : "
    )
    if y == "a":
        addProject(usrMail)
    elif y == "v":
        viewProjects()
    elif y == "e":
        editProject(usrMail)
    elif y == "d":
        deleteProject(usrMail)
    elif y == "s":
        searchProjects()
    else:
        print("invalid option")
        projectMenu(usrMail)
