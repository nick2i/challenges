# 
# each queen has two intersecting diagonal lines
# and must not find any queens on those diagonals
# 
# for a queen at x1 y1, the diagonals are
# f_a(x) = (x - x1) + y1
# f_b(x) = -(x - x1) + y1

def qcheck(queens):
    board_size = len(queens)
    if len(set(queens)) != board_size:
        return False

    # keep track of all squares diagonally seen by queens
    seen = set()
    for x, y in enumerate(queens):
        q = y - 1
        if (x, q) in seen:
            print(f"queen at {(x,q)} is seen by some other queen")
            return False
        for x_i in range(board_size):
            if x_i == x:
                continue
            y_i_a = (x_i - x) + q
            y_i_b = -(x_i - x) + q
            seen.add((x_i, y_i_a))
            seen.add((x_i, y_i_b))

def main():
    tests = [
        ([4, 2, 7, 3, 6, 8, 5, 1], True),
        ([2, 5, 7, 4, 1, 8, 6, 3], True),
        ([5, 3, 1, 4, 2, 8, 6, 3], False),
        ([5, 8, 2, 4, 7, 1, 3, 6], False),
        ([4, 3, 1, 8, 1, 3, 5, 2], False),
    ]
    
    for queens, expected in tests:
        result = qcheck(queens)
        print(f"{result = }\t\t{expected = }")

if __name__ == "__main__":
    main()

