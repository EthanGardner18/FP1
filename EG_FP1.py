# In this problem I was to code the greedy algorithm of mice to holes. My design is I sort the mice and the holes and line them up in the array. 
# Me and my partner were able to sovle the mice to holes problem correctly. 
# I personally didn't run into any more issues switching from the psuedo code I wrote and the tips she gave me. 

def MTH(mices, holes, n, m):
    # If there are more mice then holes stop
    if (m > n):
        return -1
    
    # Start by sorting the mice and the holes. The sort function used is the standard sort function in python. It sorts them in ascending order
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
    # Position of mice and holes
    # Edit these arrays to test different values, note there cannot be more mice then holes for this to work. 
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
