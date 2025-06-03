from typing import List
class Solution:
    def canCross(self, stones: List[int], current_idx: int, prev_jump: int) -> bool:
        """
        This function checks whether we can cross the stones from the current index to the end.
        It takes three parameters: the list of stones, the current index, and the previous jump.
        
        The function returns True if we can cross the stones and False otherwise.
        
        The function uses a recursive approach to explore all possible jumps from the current stone.
        It first checks if the current stone is the last stone. If it is, it returns True.
        
        Then it iterates over all possible jumps from the current stone. For each jump, it checks if the
        stone that we will land on is in the list of stones. If it is, it calls itself with the new
        current index and the jump.
        
        If any of the recursive calls return True, it means we can cross the stones, so the function
        returns True. If none of the recursive calls return True, it means we can't cross the stones,
        so the function returns False.
        """
        n = len(stones)

        if current_idx == n-1:
            return True
        
        for jump in range(prev_jump-1, prev_jump+2):
            if jump > 0 and stones[current_idx] + jump in map:
                if self.canCross(stones, map[stones[current_idx] + jump], jump):
                    return True
        return False
    
    def CanCrossMemo(self, stones: List[int], current_idx: int, prev_jump: int, dp) -> bool:

        n = len(stones)

        if current_idx == n-1:
            return True
        
        if dp[current_idx][prev_jump] != -1:
            return dp[current_idx, prev_jump]
        
        for jump in range(prev_jump-1, prev_jump+2):
            if jump > 0 and stones[current_idx] + jump in map:
                if self.canCross(stones, map[stones[current_idx] + jump], jump):
                    dp[current_idx][prev_jump] = True
                    return True
        dp[current_idx][prev_jump] = False
        return dp[current_idx][prev_jump]

stones = [0,1,3,5,6,8,12,17]
map = {stone: i for i, stone in enumerate(stones)}

solution = Solution()
print(solution.canCross(stones, 0, 0))

print(solution.CanCrossMemo(stones, 0, 0, dp=[[-1] * 2001] * 2001))
