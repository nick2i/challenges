
def is_kaprekar(n):
    n2 = n*n
    splits = []
    for i in range(1, len(str(n2))):
        splits.append((
            int(str(n2)[:i]),
            int(str(n2)[i:])
        ))
    return any(split[0] + split[1] == n for split in splits)


def kaprekar(a, b):
    return [i for i in range(a, b + 1) if is_kaprekar(i)]

def main():
    tests = [
        # ((a, b), [expected results])
        ((1, 50), [9, 10, 45]),
        ((2, 100), [9, 10, 45, 55, 99, 100]),
        ((101, 9000), [297, 703, 999, 1000, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777]),
    ]

    for test in tests:
        a, b = test[0]
        expected_result = test[1]

        result = kaprekar(a, b)
        print(f"kaprekar({a}, {b}) -> {result}")
        if result != expected_result:
            print(f"UH OH SPAGHETTIO:\n{result}\n{expected_result}\n (not equal)")

if __name__ == "__main__":
    main()
