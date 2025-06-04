def first_expression(to_double, to_triple):
    return ((2*to_double) + (3*to_triple))

def second_expression(to_double, to_triple, /):
    return ((2*to_double) + (3*to_triple))

def third_expression(to_d, to_t, *args, a, b):
    return ((2*to_d) + (3*to_t) + a - b)

answer_by_position = first_expression(4, 5)
answer_by_keyword = first_expression(to_triple=4, to_double=5)
# wanted_answer = second_expression(to_triple=4, to_double=5)
another_wanted_answer = third_expression(to_t=4, to_d=5, b=3, a=4)

print(answer_by_position)
print(answer_by_keyword)
# print(wanted_answer)
print(another_wanted_answer)

