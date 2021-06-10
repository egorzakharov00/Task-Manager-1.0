# Python program for a small business that can help it to manage tasks assigned to each member of the team

# import date from datetime
# https://docs.python.org/3/library/datetime.html
from datetime import date

# Create list for usernames
usernames = []
# Create list for passwords
passwords = []
# Create list for tasks
tasks = []

# open text file to read from
with open('user.txt', 'r') as user_file:
    # loop over each line in user_file
    for line in user_file:
        # create a temporary list with two elements being username and password
        temp = line.strip().split(", ")
        # add username and password to their according list
        usernames.append(temp[0])
        passwords.append(temp[1])

# open text file to read from
with open('tasks.txt', 'r') as tasks_file:
    # loop over each line in tasks_file
    for line in tasks_file:
        # add 2 dimensional list with tasks in outer list and task details in inner list for each task
        tasks.append(line.strip().split(", "))

# get username input from user
username = input("Enter your username:\n")

# if username is invalid loop until user enters a valid username
while username not in usernames:
    username = input("Invalid username please try again:\n")

# set target for usernames password index
target = usernames.index(username)

# get password input from user
password = input("Enter your password:\n")

# if password is invalid loop until user enters a valid password
while password != passwords[target]:
    password = input("Invalid password please try again:\n")

# create empty choice variable
choice = ''

# while choice is not exit loop over menu
while choice != 'e':
    # if user is admin show admin list of choices
    if username == 'admin':
        choice = input("Please select one of the following options:\n"
                       "r - register user\n"
                       "a - add task\n"
                       "va - view all tasks\n"
                       "vm - view my tasks\n"
                       "ds - display statistics\n"
                       "e - exit\n")

    # else show standard list of choices to non admins
    else:
        choice = input("Please select one of the following options:\n"
                       "a - add task\n"
                       "va - view all tasks\n"
                       "vm - view my tasks\n"
                       "e - exit\n")

    # registering a user that can only be done by an admin
    if choice == 'r' and username == 'admin':
        # get new username
        new_user = input("Enter a new username:\n")
        # get new password
        new_password = input("Enter a new password:\n")
        # ask to confirm password
        confirm_password = input("Confirm new password:\n")
        # if confirmed password is wrong loop until right password is entered
        while new_password != confirm_password:
            confirm_password = input("Invalid confirmation please confirm new password again:\n")
        # create result string to add to user_file
        result = "\n" + new_user + ", " + new_password
        # open text file to append to
        with open("user.txt", "a") as user_file:
            # add result to user_file
            user_file.write(result)
        # output that user has been registered
        print("User has been registered.\n")

    # adding a task
    elif choice == 'a':
        # get user who task is assigned to
        task_user = input("Enter the username of the person the task is assigned to:\n")
        # if assigned user does not exist loop until existing user is entered
        while task_user not in usernames:
            task_user = input("The username entered does not exist please try again:\n")
        # get task title, task description, date assigned and due date
        task_title = input("Enter the title of the task:\n")
        task_description = input("Enter a description of the task:\n")
        due_date = input("Enter the due date of the task in the format '1 Jan 2000':\n")
        # get today's date using date package, format accordingly and store in variable
        # https: // docs.python.org / 3 / library / datetime.html
        date_assigned = date.today().strftime('%d %b %Y')
        # create result string to add to tasks_file
        result = "\n" + task_user + ", " + task_title + ", " + task_description \
                 + ", " + date_assigned + ", " + due_date + ", No"
        # open text file to append to
        with open("tasks.txt", "a") as tasks_file:
            # add result to tasks_file
            tasks_file.write(result)
        # output that task has been added
        print("Task has been added.\n")

    # viewing all tasks
    elif choice == 'va':
        # loop over each element in tasks
        for task in tasks:
            # loop over each task and output data in a readable manner
            print("Assigned to:         " + task[0])
            print("Task:                " + task[1])
            print("Task description:    " + task[2])
            print("Date assigned:       " + task[3])
            print("Due date:            " + task[4])
            print("Task complete:       " + task[5] + "\n")

    # viewing only signed in user's tasks
    elif choice == 'vm':
        # loop over each element in tasks
        for task in tasks:
            # check if task is assigned to signed in user
            if username == task[0]:
                # Output task data in a readable manner
                print("Assigned to:         " + task[0])
                print("Task:                " + task[1])
                print("Task description:    " + task[2])
                print("Date assigned:       " + task[3])
                print("Due date:            " + task[4])
                print("Task complete:       " + task[5] + "\n")

    # if user is admin display statistics
    elif choice == 'ds' and username == 'admin':
        print("Total number of users: " + str(len(usernames)) + "\nTotal number of tasks: " + str(len(tasks)) + "\n")