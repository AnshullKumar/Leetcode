""" This is a Question from LeetCode.
Problem: 49. Group Anagrams (Medium level)


Given an array of strings strs, group the anagrams together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from collections import defaultdict  # Using a defaultdict to group anagrams

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    
    
    result = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1 
        
        result[tuple(count)].append(s)
    return result.values()

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]