date_year = (0, 1, 2, 3, 4, 5, 6, 7,8)
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

print(date_year[1:6:2])

timetable1 = slice(1, 6, 2)
print(date_year[timetable1])
timetable2 = slice(1,6)
print(date_year[timetable2])

timetable3 = slice(none, 2)
print(date_year[timetable3]) == print(date_year[:2])


# date_year.add(04); error because tuples like ds4_class are immutable

# for year in date_year:
#    print(year)

#Calender Date
print(date_year[::])

          

# Also try slices with negative starting, ending, and steps values 
