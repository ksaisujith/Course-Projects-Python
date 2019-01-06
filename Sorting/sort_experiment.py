__author__ = "Keerthi Pradhani"

'''
CSCI-603: LAB 5
Author1: SAI SUJITH KAMMARI
Author2: KEERTHI NAGAPPA PRADHANI

This program generates the random unsorted list and sorts using different algorithms and calculates the time taken.

'''
import random
import sys
import time
from instrumented_sort import *


def generate_Data(N):
    """
    This generates unsorted list with the random values from 0 to N and length of N

    :param N: The upper bound of the list
    :return: list_of_numbers  list of numbers
    """
    list_of_numbers = []
    for _ in range(N):
        # Generating random numbers and appending it to the list
        list_of_numbers.append(random.randint(0, N))
    # Shuffling the numbers in the list
    random.shuffle(list_of_numbers)
    return list_of_numbers

def check_sorted(list):
    """
    Check if the passed list is sorted or not

    :param list: list to be checked if sorted
    :return: True/False - Returns true if the list is sorted
    """
    for number in range(len(list)-1):
        # Checking if all the numbers are in order
        if list[number] > list[number+1]:
            return False
    return True

def main():
    if len(sys.argv) != 2:
        # Arguments are not passed. Hence prompting for user input
        N = input("Please provide the length of the list \n")
    elif len(sys.argv) == 2:
        # Reading the input from the command line
        N = sys.argv[1]

    # Converting the string to integer value
    N = int(N)

    # Validating the value of N
    if ( N < 0):
        print("Invalid value for N")
        sys.exit()

    # Generating the list with the random values
    unsorted_list = generate_Data(N)
    print("ALGORTHMS\t\tN\t\tComparisons\t\t\tSeconds")

    # Calculating the time taken to complete the function run
    start_time = time.time()
    results = msort(unsorted_list[:])
    time_taken = time.time() - start_time
    if (check_sorted(results[0])):
        print("MERGE\t\t\t" + str(N) + "\t\t\t" + str(results[1]) + "\t\t\t" + str(time_taken) )

    # Calculating the time taken to complete the function run
    start_time = time.time()
    results = ssort(unsorted_list[:])
    time_taken = time.time() - start_time
    if (check_sorted(results[0])):
        print("SELECTION\t\t" + str(N) + "\t\t\t" + str(results[1]) + "\t\t\t" + str(time_taken) )

    # Calculating the time taken to complete the function run
    start_time = time.time()
    results = isort(unsorted_list[:])
    time_taken = time.time() - start_time
    if (check_sorted(results[0])):
        print("INSERTION\t\t" + str(N) + "\t\t\t" + str(results[1]) + "\t\t\t" + str(time_taken) )

    # Calculating the time taken to complete the function run
    start_time = time.time()
    results = isort(unsorted_list[:])
    time_taken = time.time() - start_time
    if (check_sorted(results[0])):
        print("QUICK\t\t\t" + str(N) + "\t\t\t" + str(results[1]) + "\t\t\t" + str(time_taken) )

if __name__ == "__main__":
    main()