import random

def roll():
    total_weight = 0
    with open("list_of_hobbies.txt", "r") as file:
        while line := file.readline():
            hobby_weight_pair = line.rstrip().split(',')
            print(hobby_weight_pair)
            total_weight += int(hobby_weight_pair[1])
            print("total weight = " + str(total_weight))
        
    random_selection = random.randint(1, total_weight)
    print("random selection is " + str(random_selection))
    weight_exhausted = 0

    with open("list_of_hobbies.txt", "r") as file:
        while line := file.readline():
            hobby_weight_pair = line.rstrip().split(',')
            weight_exhausted += int(hobby_weight_pair[1])
            if(weight_exhausted >= random_selection):
                print("You get to do " + hobby_weight_pair[0] + "!!! Congrats babe")
                break

def add():
    new_hobby_name = input("What is the name of the new hobby to add? ")

    new_hobby_weight = 0
    while(new_hobby_weight < 1 or new_hobby_weight > 10):
        new_hobby_weight = int(input("What is the importance of this hobby to you on a scale of 1-10? "))

    new_hobby_line = new_hobby_name + "," + str(new_hobby_weight) + "\n"
    with open("list_of_hobbies.txt", "a") as file:
        file.write(new_hobby_line)

def main():
    # prompt the user for an input baby
    while True:
        selected_option = input("What is your desire? 'roll' to get a random hobby, 'add' to add a hobby to the list, 'quit' to quit\n")
        match selected_option:
            case "roll":
                roll()
            case "add":
                add()
            case "quit":
                break
            case _:
                print("That's not a valid option you goofball, try again")

if __name__ == "__main__":
    main()