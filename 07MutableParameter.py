def double(numbers):
    i = 0
    for number in numbers:
        numbers[i] = 2*number
        i = i + 1

marks = [30, 25, 17, 28]
print(marks)
double(marks)
print(marks)
