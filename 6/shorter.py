def int2roman(n):
    return "".join(s * (n // d) + ((n:=n%d) * 0) * "" for s, d in [(lambda k, c: [(c[k//2], pow(10, k // 4)), (c[k//2:k//2+2], 4 * pow(10, k // 4)), (c[k//2], 5 * pow(10, k // 4)), (c[k//2-1:k//2+2:2], 9 * pow(10, k // 4))][k % 4])(j, "IVXLCDM") for j in range(13)][::-1])

def main():
    for test in range(4001):
        print(f"n = {test}\t roman = {int2roman(test)}")

if __name__ == "__main__":
    main()

