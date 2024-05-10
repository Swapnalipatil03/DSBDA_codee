# Define a function to remind the user's name
def remind_name():
    # Prompt the user to remind their name
    print("Please, remind me your name.")
    # Take user input for their name
    name = input()
    # Print a message using the user's name
    print("What a great name you have, {0}".format(name))
    
# Define a function to guess the user's age based on remainders
def guess_age():
    # Prompt the user to enter remainders of dividing their age by 3, 5, and 7
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5, and 7 respectively.")
    # Take user input for remainders
    rem3 = int(input("Remainder when divided by 3: "))
    rem5 = int(input("Remainder when divided by 5: "))
    rem7 = int(input("Remainder when divided by 7: "))
    # Guess the age by iterating through possible ages
    for age in range(105):
        if age % 3 == rem3 and age % 5 == rem5 and age % 7 == rem7:
            print("Your age is {0}; that's a good time to start programming!".format(age))
            return
    # Print a message if age cannot be determined
    print("Could not determine your age. Please ensure the remainders are correct.")
    
# Define a function to count up to a specified number
def count():
    # Prompt the user to specify a number
    print("Now I will give you that I can count to any number you want.")
    num = int(input())
    # Initialize a counter and count up to the specified number
    counter = 0
    while counter <= num:
        print("{0} !".format(counter))
        counter += 1
        
# Define a function to test the user's programming knowledge
def test():
    # Print a test question and options
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To demonstrate the execution of a program.")
    print("4. To interrupt the execution of a program.")
    # Define the correct answer
    answer = 2
    # Prompt the user to input their answer
    guess = int(input())
    # Continue prompting until the correct answer is given
    while guess != answer:
        print("Please, try again.")
        guess = int(input())
    # Print a completion message when the correct answer is given
    print("Completed, have a nice day!")
    print("---------------------------")
    
# Define a function to end the program
def end():
    # Print a congratulatory message
    print("Congratulations! have a nice day!")
    print("---------------------------------")
    
# Call the defined functions in sequence
remind_name()
guess_age()
count()
test()
end()
