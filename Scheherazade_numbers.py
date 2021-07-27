def isPalindrome(n):
    flag = True
    for i in range(int(len(n)/2)):
        if n[i] != n[-i-1]:
            flag = False
            break
    if flag:
        print("It's a Palindrome!")
    else:
        print("It's not a Palindrome!")
n = input("Please enter a number:")
isPalindrome(n)