menu_options = {
    1: "Add contact",
    2: "Remove contact",
    3: "View contact book",
    4 :"Clear contact book",
    5: "Exit"
}

def print_menu():
    for key in menu_options.keys():
        print (key, "--", menu_options[key])

def run_menu():
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter menu choice:'))
        except:
            print('Please enter a number.')
        if option == 1:
            return
        elif option == 2:
            return
        elif option == 3:
            return
        elif option == 4:
            return
        elif option == 5:
            print('Thank you for using this tool!')
            exit()
        else:
            print('Please choose on of the options above.')
