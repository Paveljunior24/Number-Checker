import funktion1
from funktion2 import ispalindrome

def armstrong(num):
    """
    Checks if a number is an Armstrong number.
    
    An Armstrong number (also known as a narcissistic number) is a number that 
    is equal to the sum of its own digits each raised to the power of the number of digits.
    
    Arguments:
    num (int): The number to check.
    
    Returns:
    int: The result of the Armstrong number calculation.
    """
    result = 0
    n = len(str(num))
    temp = num
    while temp != 0:
        digit = temp % 10
        result += digit ** n
        temp //= 10
    return result

def main():
    """
    Main function to run the interactive menu for checking Armstrong numbers,
    generating Fibonacci numbers, and checking if a string is a palindrome.
    
    Continuously prompts the user to select an option until they choose to exit.
    
    Options:
    1. Check if a number is an Armstrong number.
    2. Generate a specified number of Fibonacci numbers.
    3. Check if a string is a palindrome.
    4. Exit the program.
    """
    while True:
        print("\nSelect an option from the choices below:")
        print("1. Check Armstrong number")
        print("2. Generate Fibonacci numbers")
        print("3. Check if a string is a palindrome")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            try:
                num = int(input("Enter the number to check if it is an Armstrong number: "))
                if num == armstrong(num):
                    print(f"{num} is an Armstrong number.")
                else:
                    print(f"{num} is not an Armstrong number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == 2:
            try:
                n = int(input("Enter the number of Fibonacci numbers to generate: "))
                print(f"The first {n} Fibonacci numbers are: {funktion1.fibo(n)}")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == 3:
            s = input("Enter the string to check if it is a palindrome: ")
            if ispalindrome(s):
                print(f"'{s}' is a palindrome.")
            else:
                print(f"'{s}' is not a palindrome.")
        
        elif choice == 4:
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        
        print("_" * 50)

if __name__ == "__main__":
    main()
