import icontract

@icontract.require(lambda m: (m > 15))
@icontract.require(lambda n: (n < 15))
@icontract.invariant(lambda self: ((self.m % 2) == 0))
@icontract.invariant(lambda self: ((self.n % 2) == 1))
class Couple:
    def __init__(self, m:int, n:int) -> None:
        self.m = m
        self.n = n

    @icontract.require(lambda mvi: (mvi < 10))
    def increase_m(self, mvi) -> None:
        self.m = self.m + mvi

    def increase_n(self, nvi) -> None:
        self.m = self.m + nvi

    @icontract.ensure(lambda result, m, n : (result == (m - n)))
    def m_minus_n(m: int, n: int) -> int:
        return m - n

    def __repr__(self) -> str:
        return "an instance of SomeClass"

c = Couple(28,13)
c.increase_m(4)
c.increase_n(-2)
print(c.m)
print(c.n)
