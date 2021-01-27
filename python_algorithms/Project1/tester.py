

# Test cases from: https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html


i = 1
def makeinput(i):
    with open(f'./testcases/p0{i}_c.txt') as f:
        W = int(f.read())

    with open(f'./testcases/p0{i}_p.txt') as f:
        vals = f.readlines()
        vals = [int(v) for v in vals]

    with open(f'./testcases/p0{i}_w.txt') as f:
        wts = f.readlines()
        wts = [int(w) for w in wts]

    with open(f'./testcases/p0{i}_s.txt') as f:
        sol = f.readlines()
        sol = [int(s) for s in sol]


    n = len(wts)
    items ={}
    for i in range(1,n+1):
        items[i] = (str(i), wts[i-1],vals[i-1])
    return items,W,sol


def verifyOutput(res,sol):
    mysol = set([int(k[0]) for k in res])
    correct = []
    for i,s in enumerate(sol):
        if s > 0:
            correct.append(i+1)
    correct = set(correct)
    print(mysol,correct)
    return mysol==correct



# items,W,sol=makeinput(i)
# res = knapsack(items,W)

# verifyOutput(res,sol)