lookup_table = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

def int2roman(n):
    remainder = n
    result = ""

    # by organizing lookup_table in descending order, we can
    # use a pretty simple algorithm without much branching
    for divisor, symbol in lookup_table:
        # how many divisors can we fit in the current remainder
        quotient = remainder // divisor
        # we'll need that many copies of the symbol (maybe 0)
        result += quotient * symbol
        remainder = remainder % divisor
    return result

def main():
    import random
    for _ in range(10):
        test = random.randint(1, 4000)
        roman = int2roman(test)
        print(f"test = {test},\t\troman = {roman}")

if __name__ == "__main__":
    main()
