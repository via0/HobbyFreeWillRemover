if __name__ == "__main__":
    # prompt the user for an input baby
    while True:
        selected_option = input("What is your desire? 'roll' to get a random hobby, 'add' to add a hobby to the list, 'quit' to quit\n")
        match selected_option:
            case "roll":
                print("If i was smart i would get you a hobby")
            case "add":
                print("If i was smart i would add a hobby to the list")
            case "quit":
                break
            case _:
                print("That's not a valid option you goofball, try again")