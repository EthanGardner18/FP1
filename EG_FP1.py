def assignHole(mices, holes, n, m):
    if (n != m):
        return -1
    
    mices.sort()
    holes.sort()
    
    Max = 0
     
    for i in range(n):
        if (Max < abs(mices[i] - holes[i])):
            Max = abs(mices[i] - holes[i])
     
    return Max

def main():
    mices = [ 4, -4, 2 ]
    holes = [ 4, 0, 5 ]

    n = len(mices)
    m = len(holes) 

    minTime = assignHole(mices, holes, n, m)

    print("The last mouse gets into the hole in time:", minTime)

if __name__ == "__main__":
    main()