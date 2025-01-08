"""
Given a string `s`
Find the length of the longest substring without repeating characters
- s == "whole string"
- c == "character"
- c can be letter, digits or space
- len(s) small
- c is repeated when it match duplicate wherever it is in s
  - find way to store c
  - preferabbly stored in data structure that can only contain list of unique item
- return is count of c until it match repeated c
"""


def len_substr(s: str) -> int:
    dict = {}
    count = 0
    result = 0

    for c in s:
        if c in dict:
            result = count if count > result else result
            count = 0
            dict.clear()
        dict[c] = None
        count += 1

    return result


_in = input()
print(len_substr(_in))
