class SuppRange:
    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __contains__(self, mark):
        return self.lower_bound <= mark <= self.upper_bound

wsu_dps_range = SuppRange(40, 48)
ds_mark = 42
fm_mark = 54

if ds_mark in wsu_dps_range:
    print("Your DS mark ", ds_mark, " is in the range of the dp at WSU")
else:
    print("Your DS mark ", ds_mark, " is not in the range of the dp at WSU")
    

if fm_mark in wsu_dps_range:
    print("Your FM mark ", fm_mark, " is in the range of the dp at WSU")
else:
    print("Your FM mark ", fm_mark, " is not in the range of the dp at WSU")
