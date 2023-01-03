def IsPalendrome(input):
    if len(input) == 1 or len(input) == 0:
        return True
    
    if input[0] == input[len(input)-1]:
        return IsPalendrome(input[1:-1])
    
    return False

print(IsPalendrome(input("Enter a word: ")))
