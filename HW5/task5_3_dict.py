# Print determined numbers of the Fibonacci sequence

def print_fib(n): 
    """
    This function will print determined numbers of the Fibonacci sequence.

    Params:
    n: int
    
    Returns:
    None
    """
    print("The result: ")
    for i in range(1,n+1):
        print(number_fib(i), end = " ")
    print("")

def number_fib(n): 
    """
    This function calculates determined number of the Fibonacci sequence and returns it.

    Params:
    n: int
    
    Returns:
    int
    """
    if n in Fibonacci_sequence:
        return Fibonacci_sequence[n]
    else:
        Fibonacci_sequence[n]=(number_fib(n-1)+number_fib(n-2))
        return Fibonacci_sequence[n]

# The dictionary for storing already calculated numbers of the Fibonacci sequence 
Fibonacci_sequence = {1:0,2:1}

while True:
    user_number = input("Enter a natural number how many fibonacci numbers you want to get or press the key \"Enter\" for exit: ") 
    if user_number == "":
        print("Exit the program.")
        break
    try:
        user_number = int(user_number)
        if user_number <= 0:
            raise RuntimeError("Incorrect value!")
        print_fib(int(user_number))
    except RuntimeError:
        print("Please, enter a natural number. Try again.")
        continue   
    except ValueError:
        print("Incorrect value. Try again.")
        continue
     