def is_palindrome():
    word = input("Enter the word you want to check: ")
    if word == word[::-1]:
        print("Yes, the word: " + word + " is palindrome")
    else:
        print("No, the word: " + word + " is not palindrome")
    show_menu()
def is_prime(num):
    prime = True
    if num < 2:
        prime = False
    elif num == 2:
        prime = True
    elif num % 2 == 0:
        prime = False
    else:
        for x in range(2, num):
            if num % x == 0:
                prime = False
                break
    if prime == True:
        print("YES, The number: " + str(num) + " is a prime number")
    else:
        print("NO, The number: " + str(num) + " is not a prime number")
    show_menu()
def show_menu():
    print("Choose an Operation: ")
    print("[0] Check Palindrome\t\t[1] Check if Prime\n[99]Exit")
    ans = int(input())
    if ans == 0:
        is_palindrome()
    elif ans == 1:
        num = int(input("Enter the number you want to check: "))
        is_prime(num)
    elif ans == 99:
        print("Good Bye")
    else:
        print("You have entered an incorrect choice, Please try again!")
        show_menu()
show_menu()