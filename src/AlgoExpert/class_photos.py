
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    if redShirtHeights is None or blueShirtHeights is None or len(redShirtHeights) == 0 or len(blueShirtHeights) == 0:
        return False

    redShirtHeights.sort()
    blueShirtHeights.sort()

    team_size = len(blueShirtHeights)
    # solution
    # 1. iterate the two arrays
    # 2. check height of each item in the same index
    # 3. If the all the items in red are shorter or taller than the blue. Then return True. 
    # else return false
    # Time complexity: O(n). n is the size of the team
    # Space complexity: O(n). n is the size of the team
    
    red_shorter_count = 0
    red_taller_count = 0
    for red, blue in zip(redShirtHeights, blueShirtHeights):
        if red > blue:
            red_taller_count += 1
        elif red < blue:
            red_shorter_count += 1
    return red_shorter_count == team_size or red_taller_count == team_size

def classPhotos_optimized(redShirtHeights, blueShirtHeights):
    # Write your code here.
    if redShirtHeights is None or blueShirtHeights is None or len(redShirtHeights) == 0 or len(blueShirtHeights) == 0:
        return False
    
    # Sort both arrays
    redShirtHeights.sort()
    blueShirtHeights.sort()

    # The core logic is that ensure all the heights in either team are consistently taller or shorter
    # If the heights are not consistent, then return false

    # use a counter to keep the times when the red one is not the same as the blue one. it will not record the equal ones
    gap_times = 0
    shorter_count = 0

    # If the red item is taller compared to the blue one, then count +1, else -1. 
    team_size = len(blueShirtHeights)

    for i in range(team_size):
        if abs(shorter_count) < gap_times:
            return False

        if redShirtHeights[i] > blueShirtHeights[i]:
            shorter_count -= 1
        elif redShirtHeights[i] < blueShirtHeights[i]:
            shorter_count += 1
        else:
            # the equal case will not increase any
            return False
       
        gap_times += 1

    return gap_times == abs(shorter_count)


if __name__ == "__main__":

    redShirtHeights = [3, 5, 6, 8, 2]
    blueShirtHeights = [2, 4, 7, 5, 1]
    print(classPhotos_optimized(redShirtHeights, blueShirtHeights))