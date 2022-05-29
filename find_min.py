#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Generates 10 random numbers between 1-50 and finds the one with
# the minimum value
import random

import constants


# This function finds the number wit hthe lowest value and returns it to main
def find_min(ints):
    lowest = ints[0]
    # for each loop iterates through every spot in the array one at a time
    for a_num in ints:
        if a_num < lowest:
            lowest = a_num

    return lowest


def main():
    int_arr = []
    # Generating random numnbers
    for counter in range(constants.MAX_SIZE):
        rand_num = random.randint(constants.MIN_NUM, constants.MAX_NUM)
        # Putting random numbers into the array
        int_arr.append(rand_num)
        print("Position {} is {}".format(counter, int_arr[counter]))
    # setting a variable to the return value of find_min
    min_val = find_min(int_arr)
    print("\nThe smallest value is {}".format(min_val))


if __name__ == "__main__":
    main()
