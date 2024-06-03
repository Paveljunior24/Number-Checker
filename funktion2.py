def ispalindrome(s):
    """
    Checks if a string is a palindrome.
    
    A palindrome is a string that reads the same backward as forward.
    
    Arguments:
    s (str): The string to check.
    
    Returns:
    bool: True if the string is a palindrome, otherwise False.
    """
    return s == s[::-1]

def isprime(n):
    """
    Checks if a number is prime.
    
    A prime number is an integer greater than 1 that has no divisors other than 1 and itself.
    
    Arguments:
    n (int): The number to check.
    
    Returns:
    bool: True if the number is prime, otherwise False.
    """
    if n <= 1:
        return False  # Numbers <= 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False  # If n is divisible by i, n is not prime
    return True  # If no divisions work, n is prime
