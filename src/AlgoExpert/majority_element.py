def majorityElement(array):
    # Write your code here.
    """
    Solution (Time: O(n), Space: O(1))
    Since if there is the majority number, its count in the array should 
    be greater than the len(array) // 2.
    Which means for each element in the array, at most there are 
    n / 2 - 1, non majority element. For each element, it can be exclude from 
    the iteration for each majority element in pair.

    e.g. [1, 2, 1] -> [1] exclude with [2], then [1] left, then it is the majority
        
    """

    answer = None
    count = 0

    # [2]
    for num in array:  
        if count == 0:
            answer = num       
        
        if num == answer:
            count += 1
        else:
            count -= 1                
    
    return answer
