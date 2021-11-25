import argparse

def parse_cmd_line_arguments():   
    my_parser = argparse.ArgumentParser(
        prog="contact_book",
        description="Management tool for a contact book",
        epilog="Thank you for using "
    )

    my_parser.add_argument('--add',
                            nargs='+',
                            action='store',
                            type=str,
                            help="Add a new contact to the contact book. Set name and contact number of new entry.")
    my_parser.add_argument('--remove',
                            nargs='+',
                            action='store',
                            type=str,
                            help="Remove a contact from the contact book. Give name and contact number of entry.")

    my_parser.add_argument("--clear",
                            nargs='?',
                            help="Clear the entire contact book.")

    my_parser.add_argument("--display",
                            help="View contact book.")

    return my_parser.parse_args()

def run_args_analysis():
    args = cli.parse_cmd_line_arguments()
    database.add(args.add[0], args.add[1])
    database.remove_by_name(args.remove[0])
    database.remove_by_number(args.remove[1])

