def MTH(mices, holes, n, m):
    # If there are more mice then holes stop
    if (m > n):
        return -1
    
    # Start by sorting the mice and the holes. Then see the max difference between each one for the longest time
    mices.sort()
    holes.sort()
    
    # Set the largest distance to 0 
    max = 0
    
    #compares the location of the mice to the holes
    for i in range(n):
        if (max < abs(mices[i] - holes[i])):
            max = abs(mices[i] - holes[i])
     
    return max

def main():
    # Position of mice
    mice = [ 4, 9, 2 ]
    holes = [ 4, 0, 5 ]

    # Num of holes and num of mice
    n = len(mice)
    m = len(holes) 

    # Time for all mice to find a hole
    time = MTH(mice, holes, n, m)

    print("Total Time was ", time)

if __name__ == "__main__":
    main()