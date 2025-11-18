def f(palindrome):
    palindrome = str(palindrome)
    palindrome = palindrome.lower().replace(" ", "")
    rev_palindrome = palindrome[::-1]
    if palindrome == rev_palindrome:
        return True
    else:
        return False
    
print(f("On no"))