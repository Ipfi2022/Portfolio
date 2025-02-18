date_year = (00, 01, 02, 03, 04, 05, 06, 07,08)
print(date_year)

# Negative indexes are pythonic, but also appear in other languages
first_year = date_year[0]
print(first_year)
final_year = date_year[-1]
print(final_year)
second_year = date_year[1]
print(second_year)
year_before_last = date_year[-2]
print(year_before_last)

print(date_year[1:6])
print(date_year[1:])
print(date_year[:6])

print(date_yeat[1:6:2])

slice1 = slice(1, 6, 2)
print(date_year[slice1])
slice2 = slice(1,6)
print(date_year[slice2])

# date_year.add(04); error because tuples like ds4_class are immutable

for student in ds4_class:
    print(student)

# Also try slices with negative starting, ending, and steps values 
