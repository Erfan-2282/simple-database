print("Welcome to this simple database.")
database = {}
while True:
    print("""
        What do you want to do?
            Enter A to add a new key.
            Enter C to change a value.
            Enter D to delete a key.
            Enter E to clear the database.
            Enter S to search for a value.
            Enter K to show all keys.
            Enter V to show all values.
            Enter F to show full database.
            Enter Q to quit.
            """)
    action = input().strip().upper()
    if action == "A":
        key = input("Enter key: ")
        value = input("Enter value: ")
        database[key] = value
        print(f"{key} : {value}\nThis key has been added.")
    elif action == "C":
        key = input("Enter the key: ")
        if key in database:
            new_value = input("Enter the new value: ")
            database[key] = new_value
            print(f"{key} : {new_value}")
        else:
            print("No such key in the database.")
    elif action == "D":
        key = input("Enter key: ")
        if key in database:
            del database[key]
            print(f"{key} was deleted." )
        else:
            print("No such key in the database.")
    elif action == "E":
        database.clear()
        print("Database is cleared.")
    elif action == "S":
        key = input("Enter key: ")
        if key not in database:
            print("No such key in the database.")
        else:
            print(f"The value for the {key} key is {database[key]}.")
    elif action == "K":
        print(list(database.keys()))
    elif action == "V":
        print(list(database.values()))
    elif action == "F":
        print(database)
    elif action == "Q":
        print("Thanks for using")
        break
    else:
        print("You have not typed a valid action.")
