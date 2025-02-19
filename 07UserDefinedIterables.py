class Doubles:
    def __init__(self, first_index, last_index, step=1, touch_last=0):
        self.first_index = first_index
        self.last_index = last_index
        self.step = step
        self.touch_last = touch_last
        self._current_index = first_index

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index > self.last_index - self.touch_last:
            raise StopIteration
        else:
            self._current_index = self._current_index + self.step
            return 2*(self._current_index - self.step)

doubles0 = Doubles(5, 7)
print(next(doubles0))
print(next(doubles0))
print(next(doubles0))
print(next(doubles0))

print("\n")

doubles1 = Doubles(2, 9)
for d1 in doubles1:
    print(d1)

print("\n")

doubles2 = Doubles(2, 9, step=2)
for d2 in doubles2:
    print(d2)

print("\n")

doubles3 = Doubles(2, 9, touch_last=3)
for d3 in doubles3:
    print(d3)

