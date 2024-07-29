n = int(input("Enter a number : "))
if n > 1:
    flag = True
    for i in range(2,n):
        if (n % i == 0):
            flag = False
            break    

    if flag == False:
       print("The given number is not a prime number")
    else:
       print("The given number is prime number")

else:
    print("The given number is not a prime number")