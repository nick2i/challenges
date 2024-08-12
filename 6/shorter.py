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
    result = ""
    for divisor, symbol in lookup_table:
        quotient, n = divmod(n, divisor)
        result += quotient * symbol
    return result

def int2roman2(n):
    # already abusing syntax
    return "".join(symbol * (n // divisor) + ((n := n % divisor) * 0) * "" for divisor, symbol in lookup_table)

def int2roman3_prime(n):
    c = "IVXLCDM"
    table = []
    '''
    for i in range(3): # should be 4
        k = i * 2
        temp = c[k:k+2]
        table.extend([(c[k], pow(10, i)), (c[k:k+1], 4 * pow(10, i)), (c[k+1], 5 * pow(10, i)), (c[k:k+2:2], 9 * pow(10, i))])
    '''

    import pprint
    print(f"{len(c) = }")
    for j in range(13):
        #f = lambda k: [(c[k], pow(10, k // 2)), (c[k:k+1], 4 * pow(10, k // 2)), (c[k+1], 5 * pow(10, k // 2)), (c[k:k+2:2], 9 * pow(10, k // 2))][k % 4]
        f = lambda k: [(c[k//2], pow(10, k // 4)), (c[k//2:k//2+2], 4 * pow(10, k // 4)), (c[k//2], 5 * pow(10, k // 4)), (''.join((c[k//2-1], c[k//2+1:k//2+2])), 9 * pow(10, k // 4))][k % 4]
        print(f"{j = }\t {j // 2 = }\t {j // 4 = }\t {(j // 2) % 4 = }\t ")
        print(f"{j // 2 + 2 = }\t {(j // 2) % 4 = } ")
        table.append(f(j))
        pprint.pprint(table)

    return table

def int2roman3(n):
    t = [(lambda k, c: [(c[k//2], pow(10, k // 4)), (c[k//2:k//2+2], 4 * pow(10, k // 4)), (c[k//2], 5 * pow(10, k // 4)), (c[k//2-1:k//2+2:2], 9 * pow(10, k // 4))][k % 4])(j, "IVXLCDM") for j in range(13)][::-1]
    import pprint
    pprint.pprint(t)
    r = list((s * (n // d) + ((n:=n%d) * 0) * "" for s, d in [(lambda k, c: [(c[k//2], pow(10, k // 4)), (c[k//2:k//2+2], 4 * pow(10, k // 4)), (c[k//2], 5 * pow(10, k // 4)), (c[k//2-1:k//2+2], 9 * pow(10, k // 4))][k % 4])(j, "IVXLCDM") for j in range(13)][::-1]))
    pprint.pprint(r)
    return "".join(s * (n // d) + ((n:=n%d) * 0) * "" for s, d in [(lambda k, c: [(c[k//2], pow(10, k // 4)), (c[k//2:k//2+2], 4 * pow(10, k // 4)), (c[k//2], 5 * pow(10, k // 4)), (c[k//2-1:k//2+2], 9 * pow(10, k // 4))][k % 4])(j, "IVXLCDM") for j in range(13)][::-1])



def main():
    import random
    for _ in range(10):
        test = random.randint(1, 4000)
        roman = int2roman(test)
        roman2 = int2roman2(test)
        roman3 = int2roman3(test)

        if roman != roman3:
            print(f"OOF OOF OOF OOF OOF {roman = }\t\t{roman3 = }")
        print(f"test = {test},\t\troman = {roman}")

if __name__ == "__main__":
    main()
    #print(int2roman3(1))
