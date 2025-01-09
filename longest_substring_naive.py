"""
Given a string `s`, find the length of the longest
substring without repeating characters.
- what makes character repeated
  - when character occured more than 1
- what make a substring
  - any sequence of character inside a string

bruteforce:
- start counting from character 1 until it match its duplicate
- when repeated are detected, move to the next character and start over again until the end
- max(results)
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        results = [0]
        _set = set()
        for i, pin in enumerate(s):
            results.append(0)
            for char in s[i:]:
                if char in _set:
                    _set = set()
                    break
                _set.add(char)
                results[i] += 1
        return max(results)


"""
The bruteforce solution are accepted, but we can improve this more using
dynamic programming. 
"""
