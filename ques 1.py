def number1program():
    numbers = input("Enter the elements: ")
    target = int(input("Which element are you searching for: "))

    newlist = numbers.split(",")
    count = 0

    for i in newlist:
        if int(i) == target:
            count += 1

    return count

print(number1program())