
def rotateMatrix(matrix, direction):
    step = 1 - 2*(direction[1] == 'l')
    return list(list(mid) for mid in zip(*matrix[::step]))[::-step]

def main():
    import pprint
    debug = True
    tests = [
        # (
        #     [ input ],
        #     [ expected clockwise output ],
        #     [ expected counterclockwise output ],
        # ),
        (
            [['x']*3, ['y']*3, ['z']*3],
            [['z', 'y', 'x']]*3,
            [['x', 'y', 'z']]*3,
        ),
        (
            [list(range(10))]*3,
            [[i]*3 for i in range(10)],
            [[9 - i]*3 for i in range(10)],
        ),
    ]

    for matrix, clockwise, ctrclockwise in tests:
        clockwise_result = rotateMatrix(matrix, 'clockwise')
        ctrclockwise_result = rotateMatrix(matrix, 'counterclockwise')
        if debug:
            fstring_expression = '\n '.join(pprint.pformat(mid) for mid in matrix)
            result_cannot = '\n '.join(pprint.pformat(mid) for mid in clockwise_result)
            contain_backslash = '\n '.join(pprint.pformat(mid) for mid in ctrclockwise_result)
            print(f"Rotating matrix:\n {fstring_expression}\nClockwise:\n {result_cannot}\nCounterclockwise:\n {contain_backslash}\n")
        if clockwise != clockwise_result:
            print(f"clockwise mismatch for\n{matrix}\nexpected:\n{clockwise}\nobserved:\n{clockwise_result}")
        if ctrclockwise != ctrclockwise_result:
            print(f"counterclockwise mismatch for\n{matrix}\nexpected:\n{ctrclockwise}\nobserved:\n{ctrclockwise_result}")
    print("done :)")

if __name__ == "__main__":
    main()
