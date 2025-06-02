from typing import List

class Solution:

    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        used_in_level = [beginWord]
        queue = [[beginWord]]
        current_level = 0
        results = []

        while queue:
            path = queue.pop(0)

            # Check if we've moved to a new level and removed all the words used in the previous level
            if len(path) > current_level:
                current_level += 1
                for word in used_in_level:
                    word_set.discard(word)
                used_in_level = []

            last_word = path[-1]
            if last_word == endWord:
                if not results:
                    results.append(path)
                elif len(results[0]) == len(path):
                    results.append(path)

            # Generate all valid next words
            for i in range(len(last_word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = last_word[:i] + c + last_word[i + 1 :]
                    if next_word in word_set:
                        queue.append(path + [next_word])
                        used_in_level.append(next_word)
        return results

'''
This code implements a solution to the Word Ladder II problem, where we find all shortest transformation sequences from a given begin word to an end word using a list of valid words.
The algorithm uses a breadth-first search (BFS) approach to explore all possible transformations, keeping track of the current level and the words used in that level to avoid revisiting them.
'''
# Example usage:
sol = Solution()
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(sol.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
