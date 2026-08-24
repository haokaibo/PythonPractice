def arrayOfProducts(array):
    # Write your code here.
    """
    Solution (Time:O(n), Space: O(n))
    [A, B, C]
    [B x C, A x C, A x B]
        [B]
    [A]    [C]
    
    1. Use two arrays to hold the element index : previous products
    2. Iterate the array, to calculate the accumulated proudct from the front and end

    first_half = []

    later_half = []

    array[i] = first_half[i-1] * later_half[i+1]
    
    """
    n = len(array)

    # if n == 1:
    #     return array
    
    first_half = [1] * n
    second_half = [1] * n
    result = []
    
    for i in range(1, n):
        first_half[i] = array[i - 1] * first_half[i - 1]
        second_half[n - i - 1] = array[n - i] * second_half[n - i]

    result = [j * k for j, k in zip(first_half, second_half)]
    
    return result





