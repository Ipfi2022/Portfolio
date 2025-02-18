ds4_class = ("Mosuli", "KG", "Juza", "Liyema", "Peko", "Sam", "Nota", "Tongo")
print(ds4_class)

# Negative indexes are pythonic, but also appear in other languages
first_student = ds4_class[0]
print(first_student)
last_student = ds4_class[-1]
print(last_student)
second_student = ds4_class[1]
print(second_student)
student_before_last = ds4_class[-2]
print(student_before_last)

print(ds4_class[1:6])
print(ds4_class[1:])
print(ds4_class[:6])

print(ds4_class[1:6:2])

slice1 = slice(1, 6, 2)
print(ds4_class[slice1])
slice2 = slice(1,6)
print(ds4_class[slice2])

# ds4_class.add("Zuma"); error because tuples like ds4_class are immutable

for student in ds4_class:
    print(student)

# Also try slices with negative starting, ending, and steps values 
