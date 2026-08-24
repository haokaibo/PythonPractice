def optimized_spiralTraverse(array):
    result=[]
    startRow, endRow = 0, len (array) - 1
    startCol, endCol = 0, len(array [0]) - 1
    
    while startRow <= endRow and startCol <= endCol: 
        #right
        for col in range(startCol, endCol + 1) :
            result.append (array [startRow][col])
        #down
        for row in range(startRow + 1, endRow + 1) : 
            result.append (array [row] [endCol])
        #left
        for col in reversed (range (startCol, endCol)) :
            result.append (array[endRow][col])
        #up
        for row in reversed (range(startRow + 1, endRow)) :
            result.append (array[row] [startCol])

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -=1

    return result

def spiralTraverse(array):
    # Write your code here.
    """
    Solution(Time: O(m x n), Space: O(n))
    1 2 3
    8 9 4
    7 6 5

    1. Define some helper functions for the move. 
    right(array, begin, end)
    down(array, begin, end)
    left(array, begin, end)
    up(array, begin, end)
    2. Keep updating the right, down, left and up boundary after each move. e.g. When left move completed the up boundary should decrease 1.
    3. Stop condition when begin > end
    """
    flattened_array = []
    up = -1
    down = len(array)
    left = -1
    right = len(array[0])
    row = 0
    col = -1
    while len(flattened_array) < len(array) * len(array[0]):
        # move right
        col += 1
        while col < right:
            if addElement(flattened_array, array, row, col):
                return flattened_array
            col += 1
        up += 1
        col -= 1
        
        # move down
        row += 1
        while row < down:
            if addElement(flattened_array, array, row, col):
                return flattened_array
            row += 1
        right -= 1
        row -= 1

        # move left
        col -= 1
        while col > left:
            if addElement(flattened_array, array, row, col):
                return flattened_array
            col -= 1
        down -= 1
        col += 1
        
        # move up
        row -= 1
        while row > up:
            if addElement(flattened_array, array, row, col):
                return flattened_array
            row -= 1
        left += 1
        row += 1

    return flattened_array

def addElement(flattened_array, array, row, col):
    flattened_array.append(array[row][col])
    return len(flattened_array) == len(array) * len(array[0])

print(optimized_spiralTraverse([
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]]))
