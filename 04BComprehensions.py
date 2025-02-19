triples_list = [3*i for i in range(10)]
triples_set = {3*i for i in range(10)}
triples_dict = {i:3*i for i in range(10)}

odds_doubles = [2*i for i in range(10) if (i % 2 != 0)]
points = [(n, m) for n in range(2,5) for m in range(3)]

print(triples_list)
print(triples_set)
print(triples_dict)
print(odds_doubles)
print(points)
