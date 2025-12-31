def runLengthEncoding(string):
    # Write your code here.
    # Solution
    # Time complexity: O(n)
    # Space complexity: O(n)
    # Create an array to hold compressed characters.
    array = []
    counter = 1
    # Iterate the string object, use a variable to hold the previous character
    # A
    # if len(string) == 1:
    #     return f"1{string}"

    # AAB -> 2AB
    for i in range(1, len(string)):
        
        if string[i-1] != string[i] or counter == 9:                
            array.append(f"{counter}{string[i-1]}")
            counter = 1
        else:
            counter += 1

    # Handle the last character
    array.append(f"{counter}{string[len(string)-1]}")
    # join the elements in the array to a string as the return
    return "".join(array)
