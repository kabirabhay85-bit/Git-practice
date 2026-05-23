n = int(input("Enter your number : "))

if n>1:
    for i in range (2,n):
        if n%i == 0:
            print("Given number is not prime number")
            break
    else:
        print("given number is prime number")