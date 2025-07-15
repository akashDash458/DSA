"""
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""


def get_palin_(s, l, r, res):
    new_res = res
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 > len(new_res):
            new_res = s[l : r + 1]
        l -= 1
        r += 1
    return new_res


def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        # odd_length
        res = get_palin_(s, i, i, res)
        # even_length
        res = get_palin_(s, i, i + 1, res)
    return res


print(longestPalindrome("babad"))
