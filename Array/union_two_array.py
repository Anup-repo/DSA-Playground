class Solution:
    def findUnion(self,arr1,arr2,n,m):
        i , j = 0, 0
        ans = []
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if len(ans) == 0 or ans[-1] != arr1[i]:
                    ans.append(arr1[i])
                i += 1
            else:
                if len(ans) == 0 or ans[-1] != arr2[j]:
                    ans.append(arr2[j])
                j += 1
        while i < n:
            if len(ans) == 0 or ans[-1] != arr1[i]:
                ans.append(arr1[i])
            i += 1
        while j < m:
            if len(ans) == 0 or ans[-1] != arr2[j]:
                ans.append(arr2[j])
            j += 1
        return ans
    
sol = Solution()
arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5,6,7,8,9]
print(sol.findUnion(arr1, arr2, len(arr1), len(arr2)))
