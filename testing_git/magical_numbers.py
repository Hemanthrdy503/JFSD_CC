def is_magic_number(num):
    while num > 9:
        total = 0

        while num > 0:
            total += num % 10
            num //= 10

        num = total

    return num == 1


n = int(input("Enter a number: "))

if is_magic_number(n):
    print("Magic Number")
else:
    print("Not a Magic Number")