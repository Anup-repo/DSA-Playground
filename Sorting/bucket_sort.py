# Bucket Sort Implementation
# --------------------------
# For fractional numbers in [0, 1):
# Best-case TC: O(n + k) (if uniformly distributed)
# Worst-case TC: O(n^2) (if all elements go into one bucket)
# SC: O(n + k)
# Explanation: Bucket sort divides input into buckets, sorts each bucket, and concatenates results. For fractional numbers, each bucket covers a sub-range of [0, 1).


class Solution:
    def bucket_sort_fractional(self, arr):
        n = len(arr)
        bucket = [[] for _ in range(n)]
        for num in arr:
            bi = int(num * n)
            bucket[bi].append(num)
        for b in bucket:
            b.sort()
        idx = 0
        for b in bucket:
            for num in b:
                arr[idx] = num
                idx += 1
        return arr

    # For integer numbers:
    # Explanation: Buckets are created based on the range of input integers (min to max).
    # Each integer is assigned to a bucket using its value and bucket size.
    # After distribution, each bucket is sorted individually, then concatenated.
    # This works well for uniformly distributed data; otherwise, performance may degrade.
    def bucket_sort_integer(self, arr):
        min_val, max_val = min(arr), max(arr)
        n = len(arr)
        bucket_count = max(1, n // 2)  # heuristic: fewer buckets for sparse data
        bucket_size = max(1, (max_val - min_val + 1) // bucket_count)
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            bi = min(bucket_count - 1, (num - min_val) // bucket_size)
            buckets[bi].append(num)

        for b in buckets:
            b.sort()
        idx = 0
        for b in buckets:
            for num in b:
                arr[idx] = num
                idx += 1
        return arr


# Example usage:
sol = Solution()
# Fractional bucket sort
fractional_arr = [0.12, 0.42, 0.37, 0.89, 0.26, 0.95]
print("Fractional bucket sort:", sol.bucket_sort_fractional(fractional_arr))
# Integer bucket sort
integer_arr = [1, 3, 2, 4, 6, 1]
print("Integer bucket sort:", sol.bucket_sort_integer(integer_arr))
