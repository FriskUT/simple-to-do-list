ascii_art = r'''

                                                                      
,--------.             ,------.             ,--.   ,--.        ,--.   
'--.  .--',---. ,-----.|  .-.  \ ,---.     |  |   `--' ,---.,-'  '-. 
   |  |  | .-. |'-----'|  |  \  :| .-. |    |  |   ,--.(  .-''-.  .-' 
   |  |  ' '-' '       |  '--'  /' '-' '    |  '--.|  |.-'  `) |  |   
   `--'   `---'        `-------'  `---'     `-----'`--'`----'  `--'   
                                                                      

'''
question = "What do you want to do?"
options = '''
[1] Add something to the list
[2] Remove something from the list
[3] See the current list
[4] Exit
'''
horizontal_options = '''[1] Add something to the list [2] Remove something from the list [3] See the current list [4] Exit'''
# This prints the beginning text with ASCII art, a question and options for the user.
def beggining_function():
    print(ascii_art)
    print(question)
    print(options)

beggining_function()

# This function uses a txt file to store a list of items, making the list last pernamently between runs.
def add_to_list():
    add_item = input("What do you want to add? Add only one thing at a time.:")
    with open("list.txt", "a") as file:
        file.write(add_item + "\n")
    
# This function removes a item from the list, by reading the contents and rewriting the file without the specified item.
def remove_from_list():
    # This asks the user for the item they want to remove. If they don´t type the exact text, the script will automatically crash.
    # It is planned to fix the bug that makes the script crash if the user types something that is not in the list.
    remove_item = input("What do you want to remove? Please type the exact text of the item you want to remove:")
    with open("list.txt", "r") as file:
        lines = file.readlines()
    with open("list.txt", "w") as file:
        for line in lines:
            if remove_item not in line:
                file.write(line)

def print_options():
    print(horizontal_options) # This function prints the options for the user, in case they just completed another function.
            
# This function reads the contents of the list, makes a variable with the contents and prints it.    
def see_list():
    with open("list.txt", "r") as file:
        contents = file.read() # reads the contents of the file
    print(contents)  # prints everything in the file
    

while True:
    try:
        option = int(input("Please choose a option:"))
    except ValueError:
        print("Please enter a valid number.") # This will happen if the user types something that is not a number.
        continue

    if option == 1:
        add_to_list()
        print_options()
    elif option == 2:
        remove_from_list()
        print_options()
    elif option == 3:
        see_list()
        print_options()
    elif option == 4:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a valid option from the menu")
        print_options()
