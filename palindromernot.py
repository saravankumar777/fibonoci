###gven number is palindrome are not###
num=int(raw_input("Enter a number:"))
try:
    val=int(num)
    if num==str(num)[::-1]:
        print("The given number is palindrome ")
    else:
        print("The given number is not palindrome" )
except ValueError:
     print("That's not a valid number,Try Again")
