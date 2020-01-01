#Supports are stored as six values.  The first three are
#if the support has a reaction in x,y, or moment [Bool] and The
#following three are their vlaues
supports = []
loads = []
def addLoad(type):
    print("Type of Load:")
    print("\t1. Point Load")
    print("\t2. Point Moment")
    print("\t3. Distributed Load")

    loads.append([type, 0, 0, 0, 0])
