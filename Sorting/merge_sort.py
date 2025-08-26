class Solution:
    """
    Merge Sort is a divide-and-conquer sorting algorithm that divides the array into halves,
    recursively sorts each half, and then merges the sorted halves.

    How it works:
        1. Divide the array into two halves.
        2. Recursively sort each half.
        3. Merge the two sorted halves into a single sorted array.

    Example:
        arr = [5, 1, 4, 2, 8]
        After sorting: [1, 2, 4, 5, 8]

    Time Complexity:
        O(n log n) in all cases (worst, average, best)
    Space Complexity:
        O(n) (due to temporary arrays used for merging)
    """

    def merge(self, arr, low, mid, high):
        temp = []
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def mergeSort(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)


arr = [5, 1, 4, 2, 8]
sol = Solution()
sol.mergeSort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 2, 4, 5, 8]
