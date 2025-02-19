class Division:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __enter__(self):
        print("\nDeviding ", self.n1, " by ", self.n2, " Right?")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("\nWe are tyding up a few things now.\nThanks for your patience")
        print("Execution type:", exc_type)
        print("Execution value:", exc_value)
        print("Traceback:", traceback)
        if (traceback is None):
            print("Quotient successfully calculated")
        else:
            print("Error when calculating the quotient")

    def quotient(self):
        return(self.n1 / self.n2)


with Division(3, 2) as d1:
    print(d1.quotient())

print("\n\n")

with Division(3, 0) as d2:
    print(d2.quotient())
