def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check length
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check if starts with at least two letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    
    # Check for no periods, spaces, or punctuation marks
    if not s.isalnum():
        return False
    
    # Check that numbers, if present, are at the end and do not start with 0
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == '0' or not s[i:].isdigit():
                return False
            break
    
    return True

main()
