class Doubles:
    def __init__(self, first_index, last_index, step=1, touch_last=0):
        self.first_index = first_index
        self.last_index = last_index
        self.step = step
        self.touch_last = touch_last
        self._range = self._create_range()

    def _create_range(self):
        values = []
        current_index = self.first_index
        while current_index < self.last_index - self.touch_last:
            values.append(2*current_index)
            current_index = current_index + self.step
        return values

    def __getitem__(self, index):
        return self._range[index]

    def __len__(self):
        return len(self._range)

doubles0 = Doubles(5, 9)
for d0 in doubles0:
    print(d0)
print(doubles0[0])
print(doubles0[1])
print(doubles0[2])
print(doubles0[-1])
print(doubles0[2:])
#print(doubles0[4])


print("\n")

doubles1 = Doubles(2, 10)
for d1 in doubles1:
    print(d1)

print("\n")

doubles2 = Doubles(2, 10, step=2)
for d2 in doubles2:
    print(d2)

print("\n")

doubles3 = Doubles(2, 10, touch_last=3)
for d3 in doubles3:
    print(d3)

