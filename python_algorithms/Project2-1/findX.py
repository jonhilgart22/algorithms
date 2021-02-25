# -*- coding: utf-8 -*-
# argparse allows the parsing of command line arguments
import argparse

# utility functions for cs 6515 projects
import GA_ProjectUtils as util

"""

findX.py - Intro to Graduate Algorithms, Summer 2020

Solve the findX in an Infinite array problem using a Divide & Conqueor method
Your runtime must be O(log n)

The array of values is indexed A[1..n] inclusive

Your code MUST NOT directly reference any variables in findX.  The following methods are available:
    
    findX.start(seed) -- returns the value (x) to search for within the array
    findX.lookup(i) -- returns A[i] or None if i>n
    findX.lookups() -- returns the number of calls to lookup

"""


def findXinA(x, findX):
    def binary_search(findX, current_index, previous_index):
        indexes_checked = []
        c = 1
        while True:
            mid_point_index = int((previous_index + current_index) / 2)
            while mid_point_index in indexes_checked:
                mid_point_index = int((previous_index + current_index - c) / 2)
                c -= 1

            print(indexes_checked, "indexes_checked")
            indexes_checked.append(mid_point_index)
            print(f"mid_point_index = {mid_point_index}")
            print(f"current_index = {current_index}")
            print(f"previous_index = {previous_index}")

            mid_point_lookup_num = findX.lookup(mid_point_index)

            print(f"mid_point_lookup_num = {mid_point_lookup_num}")
            if mid_point_lookup_num is None:  # we've gone too far
                current_index = mid_point_index - 1
            elif mid_point_lookup_num == number_searching_for:  # did we find it?
                theIndex = mid_point_index
                print(f"Found the index at {theIndex}")
                return theIndex
            elif mid_point_lookup_num > number_searching_for:  # to the right or left?
                print("to the left")
                current_index = mid_point_index - 1
            elif mid_point_lookup_num < number_searching_for:  # to the right or left?
                print("to the right")
                previous_index = max(mid_point_index, previous_index) + 1
            print("---------------------")

    # TODO Your Code Begins Here, DO NOT MODIFY ANY CODE ABOVE THIS LINE
    # need to do exponential search + binary search
    number_searching_for = findX.x
    print(number_searching_for, "number_searching_for")

    current_index = 1
    previous_index = 1
    while True:
        print(f"current_index = {current_index}")
        print(f"previous_index = {previous_index}")
        current_index_num = findX.lookup(current_index)
        print(f"current_index_num = {current_index_num}")
        print("---")
        if current_index_num == number_searching_for:
            theIndex = current_index
            break
        elif (
            current_index_num is None or current_index_num > number_searching_for
        ):  #  return the value ofA[index], orNoneifindex > n
            # conduct binary search
            print("Conducting binary search")
            theIndex = binary_search(
                findX, min(current_index, number_searching_for - 1), previous_index
            )
            break

        else:
            if current_index == 1:
                current_index += 1
            previous_index = current_index
            current_index = int(current_index * 2)

    # theIndex = None  # replace None with the index of x

    # TODOne Your code Ends here, DO NOT MOIDFY ANYTHING BELOW THIS LINE

    numLookups = findX.lookups()

    print(numLookups, "numLookups")

    return theIndex, numLookups


def main():
    """
    main - DO NOT CHANGE ANYTHING BELOW THIS LINE
    """
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    parser = argparse.ArgumentParser(description="Find X Coding Quiz")

    # args for autograder, DO NOT MODIFY ANY OF THESE
    parser.add_argument(
        "-n",
        "--sName",
        help="Student name, used for autograder",
        default="GT",
        dest="studentName",
    )
    parser.add_argument(
        "-a",
        "--autograde",
        help="Autograder-called (2) or not (1=default)",
        type=int,
        choices=[1, 2],
        default=1,
        dest="autograde",
    )
    parser.add_argument(
        "-s",
        "--seed",
        help="seed value for random function",
        type=int,
        default=123456,
        dest="seed",
    )
    parser.add_argument(
        "-l", "--nLower", help="lower bound for N", type=int, default=10, dest="nLower"
    )
    parser.add_argument(
        "-u",
        "--nUpper",
        help="upper bound for N",
        type=int,
        default=100000,
        dest="nUpper",
    )

    args = parser.parse_args()

    # DO NOT MODIFY ANY OF THE FOLLOWING CODE

    findX = util.findX()
    x = findX.start(args.seed, args.nLower, args.nUpper)
    index, calls = findXinA(x, findX)
    print("findX result: x found at index {} in {} calls".format(index, calls))

    return


if __name__ == "__main__":
    main()
