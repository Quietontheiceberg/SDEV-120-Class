numbers = []
max_size = 15

for i in range (1, max_size + 1):
        number = int(input("Number " + str(i) + ": "))
        numbers.append(number)
total = max_size

for i, num in enumerate(numbers, start=1):
    if num % 2 == 0:
        print(f"{i}: {num} is even")
    else:
        print(f"{i}: {num} is odd")

print(numbers)

