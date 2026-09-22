def is_palindrome_recursive(word):
    
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_recursive(word[1:-1])
            

# word = input('Palavra: ').lower()

# if is_palindrome_recursive(word):
#     print(f'{word} é palíndroma.')
# else:
#     print(f'{word} não é palíndroma.')