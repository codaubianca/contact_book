import sys
from rpcontacts import simple_menu, cli

CURRENT_VIEW = 0

def main():

    if CURRENT_VIEW == 0:
        simple_menu.run_menu()
    elif CURRENT_VIEW == 1:
        cli.run_args_analysis()
    # elif CURRENT_VIEW == 2:
    # run GUI (TODO)


    return 


