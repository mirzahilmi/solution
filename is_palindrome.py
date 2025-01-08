def is_palindrome(word: str) -> bool:
    return word == word[::-1]


input = input()
result = is_palindrome(input)
print(f"{input} is {'palindrome' if result else 'not palindrome'}")
