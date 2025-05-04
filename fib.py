def fibonacci(num):
    """
    This is a Fibonacci sequence returning the sequence for a given number of values.

    Parameters:
        num (int): The number of sequence values to return.

    Returns:
        List - The returns num values in the sequence as a list.
    """
    # Initialize the function with an empty list
    fib_list = []

    # Initialize the sequence values (current and next)
    a, b = 0, 1

    # Loop through the number of sequences to process appending new values to a list.
    for i in range(num):
        fib_list.append(a)
        a, b = b, a+b

    # Return the list of fibonacci sequence value.
    return fib_list


def main():
    """
    main function to request input for how many numbers in the Fibonacci sequence to return.
    Call the fib generator.
    Print each item in the sequence.
    """

    # Prompt user to input
    fib_count = int(input('Provide how many numbers in the Fibonacci sequence to return: '))

    # Call the fibonacci sequence function and print the results.
    print(fibonacci(fib_count))


if __name__ == "__main__":
    main()
