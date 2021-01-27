# -*- coding: utf-8 -*-
# argparse allows the parsing of command line arguments
import argparse
from tester import makeinput  # TODO: remove

# utility functions for cs 6515 projects
import GA_ProjectUtils as util

"""
Initialize the table to be used to record the best value possible for given 
item idx and weight
NOTE : this table must be 2 dimensional (i.e. T[x][y])
"""


def initTable(numItems, maxWt):
    # Replace the following with your code to initialize the table properly!
    T = list_of_lists = [[0 for col in range(maxWt + 1)] for row in range(numItems + 1)]

    return T


"""
Build item iterator - iterator through all available items
    numItems : number of items
"""


def buildItemIter(numItems):
    # Replace the following with your code to build the item iterator!
    return range(numItems + 1)


"""
Build weight iterator - iterator of all possible integer weight values
    maxWt : maximum weight available
"""


def buildWeightIter(maxWt):
    # Replace the following with your code to build the weight iterator!
    return range(maxWt + 1)


"""
Define the subproblem to solve for each table entry - set the value to be maximum for a given
item and weight value
    T : the table being populated
    iterWt : weight from iteration through possible weight values
    itemIDX : the index of the item from the loop iteration
    itemWt : the weight of the item
    itemVal : the value of the item
"""


def subProblem(T, iterWt, itemIDX, itemWt, itemVal):
    # Replace the following with your code to solve the subproblem appropriately!

    if itemIDX == 0 or itemWt == 0:
        return 0
    if itemWt <= iterWt:
        return max(itemVal + T[itemIDX - 1][iterWt - itemWt], T[itemIDX - 1][iterWt])
    else:
        return T[itemIDX - 1][iterWt]


"""
Construct list of tuples of items that should be chosen.  

    T : the populated table of item values, indexed by item idx and weight
    items : list of items
    maxWt : maximum weight allowed
"""


def buildResultList(T, items, maxWt):

    n_items = len(items)
    final_value_found = T[n_items][maxWt]  # 0 indexed
    list_of_items = []

    w = maxWt
    for i in range(n_items, 0, -1):  # 0 indexed items
        if final_value_found <= 0:
            break
        if final_value_found == T[i - 1][maxWt]:  # previous row has the same  element
            continue
        else:

            list_of_items.append(items[i])
            final_value_found = final_value_found - items[i][2]
            maxWt = maxWt - items[i][1] + 1
    return list_of_items


"""
Solve the knapsack problem for the passed list of items and max allowable weight
DO NOT MODIFY THE FOLLOWING FUNCTION
NOTE : There are many ways to solve this problem.  You are to solve it
        using a 2D table, by filling in the function templates above.  
        If not directed, do not modify the given code template.
"""


def knapsack(items, maxWt):
    numItems = len(items)
    # initialize table properly
    table = initTable(numItems, maxWt)
    # build iterables
    # item iterator
    itemIter = buildItemIter(numItems)
    # weight iterator
    weightIter = buildWeightIter(maxWt)

    for itmIdx in itemIter:
        # query item values from list
        if itmIdx != 0:
            item, itemWt, itemVal = items[itmIdx]
        else:
            item, itemWt, itemVal = [0, 0, 0]
        for w in weightIter:
            # expand table values by solving subproblem
            table[itmIdx][w] = subProblem(table, w, itmIdx, itemWt, itemVal)
    # build list of results - chosen items to maximize value for a given weight
    return buildResultList(table, items, maxWt)


"""
main
"""


def main():
    # DO NOT REMOVE ANY ARGUMENTS FROM THE ARGPARSER BELOW
    # You may change default values, but any values you set will be overridden when autograded
    parser = argparse.ArgumentParser(description="Knapsack Coding Quiz")
    parser.add_argument(
        "-i",
        "--items",
        help="File holding list of possible Items (name, wt, value)",
        default="defaultItems.txt",
        dest="itemsListFileName",
    )
    parser.add_argument(
        "-w",
        "--weight",
        help="Maximum (integer) weight of items allowed",
        type=int,
        default=400,
        dest="maxWeight",
    )

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
    args = parser.parse_args()

    # DO NOT MODIFY ANY OF THE FOLLOWING CODE
    # configData is a dictionary that holds relevant info for the problem
    itemsList = util.buildKnapsackItemsDict(args)
    # calculate optimal knapsack loadout
    itemsChosen = knapsack(itemsList, args.maxWeight)
    # display results
    util.displayKnapSack(args, itemsChosen)


def verifyOutput(res, sol, j=-1):
    mysol = set([int(k[0]) for k in res])
    print(res, " res")
    print(sol, "sol")
    correct = []
    for i, s in enumerate(sol):
        if s > 0:
            correct.append(i + 1)
    correct = set(correct)
    if mysol == correct:
        print(f"Test case {j} PASSED: {mysol} == {correct}")
        print(f"mysol = {mysol} correct = {correct}")
    else:
        print(f"mysol = {mysol} correct = {correct}")
        print(f"Test case {j} FAILED: {mysol} != {correct}")
        return


if __name__ == "__main__":
    for i in range(1, 9):
        items, W, sol = makeinput(i)
        res = knapsack(items, W)
        verifyOutput(res, sol, i)
    exit(0)

# if __name__ == "__main__":
#     main()
