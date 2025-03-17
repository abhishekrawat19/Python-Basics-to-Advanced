import threading
import time

def print_cube(num):
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done!")


def task():
    print("Task started...")
    time.sleep(10)
    print("Task completed!")

t = threading.Thread(target=task)
t.start()

t.join()  # Main program waits here until 't' finishes
print("Main thread finished!")
