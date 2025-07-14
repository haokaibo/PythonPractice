"""
Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue

Here we use the integers 0, 1, 2 to represent the color red, white and blue respectively.

Note: You are not suppose to use the library's sort function for this program

Example:

input : [2,0,2,1,1,0]
output: [0,0,1,1,2,2]

solution1 :
Convert this problem to sorting problem.
Using Merge sort to sort the array.

Time: O(nLog(n))
space: O(n)

solutions2:
iterate the array,
count the red, white ,blue count,
return the array [0]*red + [1]*white + [2]* blue

Time: O(n)
space: O(n)
"""


class ColorObject:
    colors = {
        0: 'red',
        1: 'white',
        2: 'blue'
    }

    def __init__(self, color):
        self.color = color

    def __str__(self):
        return ColorObject.colors[self.color]


def simple_sort(arr):
    reds = 0
    whites = 0
    blues = 0
    for c in arr:
        if c == 0:
            reds += 1
        elif c == 1:
            whites += 1
        elif c == 2:
            blues += 1
    return [0] * reds + [1] * whites + [2] * blues


def merge_sort(arr):
    if arr is None or len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    return arr


def sort_colors(colors):
    return simple_sort(colors)


colors = [2, 0, 2, 1, 1, 0]
print(sort_colors(colors))
print(sort_colors([]))
