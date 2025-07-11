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
[Any Other Number] Exit
'''
my_list = []

def beggining_function():
    print(ascii_art)
    print(question)
    print(options)

beggining_function()

def add_to_list():
    add_item = input("What do you want to add? Add only one thing at a time.:")
    my_list.append(add_item)

def remove_from_list():
    remove_item = input("What do you want to remove? Please type the exact text of the item you want to remove:")
    my_list.remove(remove_item)

def see_list():
    if not my_list:
        print("The list is empty.")
    else:
        print("Current list:")
        for item in my_list:
            print(item)

while True:
    try:
        option = int(input("Please choose a option:"))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if option == 1:
        add_to_list()
    elif option == 2:
        remove_from_list()
    elif option == 3:
        see_list()
    else:
        print("Exiting the script. Goodbye!")
        break
