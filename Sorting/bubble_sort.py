class Solution:
    """
    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order.
    After each pass, the largest unsorted element 'bubbles up' to its correct position.

    Example:
        arr = [5, 1, 4, 2, 8]
        After sorting: [1, 2, 4, 5, 8]
        First pass:
            Compare 5 and 1 → swap → [1, 5, 4, 2, 8]
            Compare 5 and 4 → swap → [1, 4, 5, 2, 8]
            Compare 5 and 2 → swap → [1, 4, 2, 5, 8]
            Compare 5 and 8 → no swap → [1, 4, 2, 5, 8]
        Second pass:
            Compare 1 and 4 → no swap
            Compare 4 and 2 → swap → [1, 2, 4, 5, 8]
            Compare 4 and 5 → no swap
            Compare 5 and 8 → no swap
        Third pass:
            Compare 1 and 2 → no swap
            Compare 2 and 4 → no swap
            Compare 4 and 5 → no swap
            Compare 5 and 8 → no swap

    Time Complexity:
        Worst/Average: O(n^2)
        Best: O(n) (when array is already sorted)
    Space Complexity: O(1) (in-place)
    """

    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            is_swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    is_swapped = True
            if is_swapped == False:
                break
        return arr

sol = Solution()
print(sol.bubbleSort([1,2,3,4,5]))