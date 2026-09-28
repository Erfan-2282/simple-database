print("\nWelcome to this simple database.\n")
database = {}
while True:
    print("\nWhat do you want to do?\n(Enter A to add a key.\n Enter C to change a value(data).\n Enter D to delete a key.\n Enter E to clear the database.\n Enter S to search for a value.\n Enter K to show all keys.\n Enter V to show all values.\n Enter F to show full database.\n Enter Q to quit.) ")
    action = input().strip()
    if action.upper() == "A":
        key = input("\nEnter key:\n")
        value = input("Enter value:\n")
        database[key] = value
        print("%s : %s\nThis key has been added." % (key, value))
    elif action.upper() == "C":
        key = input("\nEnter key:\n")
        if key in database:
            new_value = input("Enter the new value.\n")
            database[key] = new_value
            print("%s : %s" % (key, database[key]))
        else:
            print("\nNo such key in the database.")
    elif action.upper() == "D":
        key = input("\nEnter key:\n")
        if key in database:
            del database[key]
            print("%s was deleted." % (key))
        else:
            print("\nNo such key in the database.")
    elif action.upper() == "E":
        database.clear()
        print("\nDatabase was clear.")
    elif action.upper() == "S":
        key = input("\nEnter key:\n")
        if key not in database:
            print("\nNo such key in the database.")
        elif key in database:
            print("The value for the %s key is %s." % (key, database[key]))
    elif action.upper() == "K":
        print("\n", database.keys())
    elif action.upper() == "V":
        print("\n", database.values())
    elif action.upper() == "F":
        print("\n", database)
    elif action.upper() == "Q":
        print("\nThanks for use.")
        break
    else:
        print("\nYou have not typed a action.")
