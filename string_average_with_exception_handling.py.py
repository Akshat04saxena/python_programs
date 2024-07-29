#Calculate the average of list numbers and uses the exception handling concepts

def average():
    l = [l1, l2, l3, l4]
    sum = 0
    for i in range(0 , 4):
        sum = sum + l[i]
    print("Sum is :",sum)
    avg = sum/4
    print("Avg is :",avg)
    if l == []:
        try:
           return 0
        except ValueError:
            return -1

    
while True:
    try:
        l1 = int(input("Enter a first number:\n"))
        l2 = int(input("Enter a second number :\n"))
        l3 = int(input("Enter a third number :\n"))
        l4 = int(input("Enter a fourth number :\n"))
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter an integer.")

average()
