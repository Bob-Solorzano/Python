def fib(num):
    """
    This is a Fibonacci sequence using a generator.

    Parameters:
        num (int): The number of sequences to return in the sequence.

    Returns:
        Dictionary - The value for the current iteration of the sequence.
    """
    a, b = 0, 1
    for i in range(1, num+1):
        yield a
        a, b = b, a+b


def main():
    """
    main function to request input for how many numbers in the Fibonacci sequence to return.
    Call the fib generator.
    Print each item in the sequence.
    """

    # Prompt user to input
    fib_count = int(input('Provide how many numbers in the Fibonacci sequence to return: '))

    # Iterate through the fibonacci generator for specified iterations and print the value.
    for item in fib(fib_count):
        print(item)


if __name__ == "__main__":
    main()
