from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        This function implements a solution to the Word Ladder problem using a breadth-first search (BFS) approach. 
        It calculates the length of the shortest transformation sequence from the starting word (beginWord) to the 
        ending word (endWord), where each transformed word must exist in the provided word list (wordList).

        Parameters:
        - beginWord: The starting word for the transformation sequence.
        - endWord: The target word to be reached through valid transformations.
        - wordList: A list of valid words that can be used for transformations.

        Returns:
        - The length of the shortest transformation sequence from beginWord to endWord. Returns 0 if no such 
        transformation sequence exists.
        """

        wordList = set(wordList)
        q = []
        q.append((beginWord, 1))
        while q:
            ele, step = q.pop(0)
            if ele == endWord:
                return step
            for i in range(len(ele)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next = ele[:i] + c + ele[i + 1 :]
                    if next in wordList:
                        q.append((next, step + 1))
                        wordList.remove(next)
        return 0

'''
This code implements a solution to the Word Ladder problem using a breadth-first search (BFS) approach. The function `ladderLength` takes a starting word, an ending word, and a list of words, and returns the length of the shortest transformation sequence from the starting word to the ending word, where each transformed word must exist in the provided list.
If no such transformation sequence exists, it returns 0.
'''

# Example usage:
sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Output: 5
print(sol.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # Output: 0
