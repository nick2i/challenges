
def compound_yearly(principal, ror, years):
    return pow(1 + ror, years) * principal

def years_left(principal, ror, years, fixed_withdrawal):
    leftovers = principal
    for i in range(years):
        leftovers = compound_yearly(leftovers, ror, 1)
        leftovers -= fixed_withdrawal
        if leftovers <= 0:
            return i - 1, fixed_withdrawal + leftovers
    return years

def main():
    a = compound_yearly(1000, 0.05, 10)
    print(f"$1000 at 5% interest compounding annually over 10 years = {a}")

    b, last_wd = years_left(1_000_000, 0.07, 100, 100_000)
    print(f"$1,000,000 earning 7% interest pear year but less $100,000 per year will last for {b} years")
    print(f"The last withdrawal amount was {last_wd}")

if __name__ == "__main__":
    main()
