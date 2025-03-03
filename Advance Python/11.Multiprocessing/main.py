# Importing the multiprocessing module
import multiprocessing

def print_cube(num):
    """
    Function to print the cube of the given number.
    This function will be executed as a separate process.
    """
    print("Cube: {}".format(num * num * num))

def print_square(num):
    """
    Function to print the square of the given number.
    This function will be executed as a separate process.
    """
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    # Creating two processes:
    # Process p1 will run the print_square function
    # Process p2 will run the print_cube function
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))

    # Starting process 1
    p1.start()
    # Starting process 2
    p2.start()

    # Waiting until process 1 completes execution
    p1.join()
    # Waiting until process 2 completes execution
    p2.join()

    # Both processes have finished execution
    print("Done!")  # This will only print after both processes are completed
