def check_palindrome(string):
    lower_string = string.lower().replace(' ','')
    middle = len (lower_string)// 2
    check = False
    for position in range(middle):
        if lower_string[position] == lower_string[-position-1]:
            check = True
        else:
            check = False
    if check:
        print("I'ts a palindrome")
    else:
        print("It's not a palindrome")
check_palindrome("Ten animals I slam in a net")
check_palindrome("Eleven animals I slam in a net")
check_palindrome("kayak")