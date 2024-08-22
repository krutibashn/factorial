"""Module providing a function printing python version."""
import time
final_list = []

def factorial(n):
    """Function printing python version."""
    time.sleep(.1)
    factorial1 = 1
    for i in range (1,n+1):
        factorial1 = factorial1 * i
    return factorial1

def sum_factorial():
    """Function printing python version."""
    for i in range(10):
        final_list.append(factorial(i))
    result=sum(final_list)
    #print("Final SUM = {}".format(result))
    print(f"Final SUM is = : {result}")
    return result

if __name__ == "__main__":
    sum_factorial()
