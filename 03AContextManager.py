class Division:
    def __init__(hours, day, night):
        hours.day = 12
        hours.night = 12

    def __enter__(hours):
        print("\adding ", hours.day, " by ", hours.night, " Right?")
        return hours

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
