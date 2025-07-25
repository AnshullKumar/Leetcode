""" This is a question from LeetCode.
Problem: 125. Valid Palindrome (Medium level)


A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome. """

def isPalindrome(s):
    
    s = s.lower()
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char
    return new_s == new_s[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))  # Output: True