def is_palindrome(text):
    for i in range(len(text)):
        if text[-(i+1)] != text[i]:
            return 'Your text is not palindrome'

    return 'Your text is palindrome'

text = input().lower()

print(is_palindrome(text))