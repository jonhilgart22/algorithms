from findX import findXinA
import math
import random
from GA_ProjectUtils import findX

"""
Extension of the findX class that allows you to reset the lookupCount so the same 
instance can be used for multiple tests of size n. This helps speed up the test
by not creating a new one each time. Also exposes a way go get index of any value
so it can iterate over them without affecting the lookup count
"""


class ResettableFindX(findX):
    def reset(self):
        self._findX__lookupCount = 0

    def dump(self):
        print(self._findX__A)

    def get(self, x):
        return self._findX__A[x]


random.seed(123456)
findX = ResettableFindX()
errors = 0

for n in range(1, 1000):
    findX.start(n, n, n)
    for x in range(1, n + 1):
        value = findX.get(x)

        findX.reset()
        try:
            index, calls = findXinA(value, findX)
            print(x, "x")
            print(value, "Value")
            print(index, calls, " index, calls ")

            if index != x:
                print("Failed: Expected {} but was {} for n={}".format(index, x, n))
                errors = errors + 1
                break
        except Exception as err:
            print("Failed: Exception for n={} x={}, {}".format(n, x, err))
            errors = errors + 1
            break
if errors > 0:
    print("Failed {} cases".format(errors))
else:
    print("Succeeded all cases")
