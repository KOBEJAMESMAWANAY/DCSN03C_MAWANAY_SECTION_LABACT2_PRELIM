#Initialize importing random, math and platform modules
import random
import math
import platform

# Function to display system information
def display_system_info():
    print(f"System Information:\nPlatform: {platform.system()}\nMachine: {platform.machine()}\n")

# Function to generate a math question
def generate_question():
    # the code will randomly choose an operation
    operation = random.choice(['+', '-', '*', '/', 'sqrt'])
    
    # Function for square root operation
    if operation == 'sqrt':
        number = random.randint(1, 100)
        return f"What is the square root of {number}?", round(math.sqrt(number), 2)
    
    # For other operations, generate two random numbers between 1 and 100 only
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    
    # This operation will calculate the answer based on the operation
    if operation == '+':
        answer = num1 + num2
    elif operation == '-':
        answer = num1 - num2
    elif operation == '*':
        answer = num1 * num2
    elif operation == '/':
        # This is to ensure that there is no division by zero
        while num2 == 0:
            num2 = random.randint(1, 100)
        answer = round(num1 / num2, 2)
    
    # Creating the question and return it along with the answer
    question = f"What is {num1} {operation} {num2}?"
    return question, answer

# Main function to run the quiz game
def main():
    display_system_info()
    print("Hi! Welcome to the Math Quiz Game!")
    
    # Asking the user how many questions they want to answer
    while True:
        total_questions = int(input("How many questions would you like to answer? "))
        if total_questions > 0:
            break
        else:
            print("Invalid input. Please enter a number greater than 0.")
    
    score = 0

    # Loop through the number of questions
    for _ in range(total_questions):
        question, answer = generate_question()
        try:
            # Ask the user the question and check their answer
            if float(input(question + " ")) == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {answer}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Display the final score
    print(f"Your final score is: {score}/{total_questions}\nThanks for playing!")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()