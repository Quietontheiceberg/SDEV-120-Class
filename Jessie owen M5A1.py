numbers = []
max_size = 15
total = int(input("Please enter 15 numbers:"))
for i in range (1, max_size + 1):
        number = int(input("Number " + str(i) + ": "))
        numbers.append(number)
total = max_size
print(numbers)
