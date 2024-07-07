from collections import defaultdict

# use prime factorization to uniquely encode text
def gen_primes():
    primes = []
    candidate = 2
    while True:
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)
            yield candidate
        candidate += 1

_primes = gen_primes()
PRIMES = [next(_primes) for _ in range(256)]

def factor(n):
    mini_n = n
    primes = gen_primes()
    factors = defaultdict(int)
    while mini_n > 1:
        p = next(primes)
        while mini_n % p == 0:
            mini_n //= p
            factors[p] += 1
    return factors

def encode(plain):
    cipher = 1
    for i, ch in enumerate(plain, start=1):
        cipher *= pow(PRIMES[ord(ch)], i)
    return cipher

def decode(cipher):
    factors = factor(cipher)
    plain = ''
    for p, _ in sorted(factors.items(), key=lambda x: x[1]):
        plain += chr(PRIMES.index(p))
    return plain

def solfege_polynomial(x):
    # thanks to our home brewed approach mentioned below this polynomial is quite reasonable
    res = -62 * pow(x, 6)
    res += 1_524 * pow(x, 5)
    res -= 13_943 * pow(x, 4)
    res += 57_618 * pow(x, 3)
    res -= 100_151 * pow(x, 2)
    res += 42_414 * x
    res += 22_680
    return res // 2_520

def scale_polynomial(x):
    # the input for this polynomial demands an extremely sensitive function, so this is less reasonable
    # also the author could not be bothered to improve readability with underscores sorry
    res = -pow(x, 11) * 443135842996879240452304560213797286793697875607902297211401067842772934037519216403703127600366333324704035467068233637494143194030021455479793429630374323757601783851
    res += pow(x, 10) * 17308951674021605333178577739784127066778735131957055065265854128674842345418311168960711955632362719373086726037653785545678044089178526674907277637043183777987225132820579539
    res -= pow(x, 9) * 270318357737453799277094975719413772913210027313536204415386008887639857085615920339373128799047796797128209535251385895120174983547609727759869774571760430012386250430577400197308017
    res += pow(x, 8) * 2109930708579853047341844930468962598118429454459443337424466088537744940464841111358434308876723873380201603481800314801878151060898113791976808571475634329207009599415341230787752363586729
    res -= pow(x, 7) * 8231484833966590362325253352165382059643293793223409426029597171706373742946135496916751154000148658838676531996873092376989066098798725764129649381549950733004513932525360633814052526587457086926
    res += pow(x, 6) * 12845786685909559133109340390315287675219759878615922030257070099375546109007295134569383508817827858792895183934740724452297741262658412063165549397198295701733633533107590718555614947360455986739435614
    res -= pow(x, 5) * 26123097313155577456629728019686326236684166522946357120708341711765554626456796933058752782390328495789157768133612799935320713357075720103009625027682239528682392273488305372227615062209014471886123312194
    res += pow(x, 4) * 22136595489145922528508759669964909727753556885265260826550614323191544501079003821379557521784841090048872247443649069785144676951475359501712655085781518078759282642358117301606489760037708337667424750237874
    res -= pow(x, 3) * 10001446959716405751021794994133668805994336142509576768799282552771797648169846022781034297545293714690256941620688768731545373202480308741351782364818112335640687153538900659098649184517232345154554984923827063
    res += pow(x, 2) * 2540799627123440051759270494660376684641464941529502205916514725893605621456160503583633268875014452324152673409170044461058563700285740472605481833569182277555988206115453465271599998166619605952883339371310127807
    res -= x * 344110427592750778392448348346490726684139952763084089874367496838790682950005255232709325859262860053302114949356139574768816829296319055190266886310636873531151550425949672549924848008534467595525620878641432382429
    res += 19410180404427408642187175207802803222951094320711358520161530764900942013182392797352008312381361767555481146824197794714605988142520307172967350932925042099489865845429093906029538326879781845523544021662082577291957
    res //= 10179547276843559814072649829571333443641370672210672972808648879059438875463197098779382231058226907670138172455053104949706552125880352965696332804937244445868625215870804230844945959924856123793866752000000
    return res

def inverse_scale_polynomial(x):
    res = -939_622_229 * pow(x, 11)
    res += 54_537_839_972 * pow(x, 10)
    res -= 1_369_379_272_360 * pow(x, 9)
    res += 19_489_918_841_085 * pow(x, 8)
    res -= 173_080_177_503_717 * pow(x, 7)
    res += 994_737_060_310_686 * pow(x, 6)
    res -= 3_713_305_043_571_970 * pow(x, 5)
    res += 8_791_927_623_674_965 * pow(x, 4)
    res -= 12_463_592_197_066_604 * pow(x, 3)
    res += 9_384_449_479_882_092 * pow(x, 2)
    res -= 2_762_634_702_391_920 * x
    res += 3_362_990_400
    return res // 9_979_200

def note(major_scale, solfege_note):
    # standardize input
    major_scale = major_scale.upper()
    solfege_note = solfege_note.upper()

    # uniquely encode major scale as an integer
    encoded_major_scale = encode(major_scale)
    # get a more manageable integer (i.e. in [0, 11])
    scale_as_integer = scale_polynomial(encoded_major_scale)

    # use a home brewed approach to transform the solfege note
    # 1. take the (unique) first character and map it to a value in [0-25]
    x = ord(solfege_note[0]) - 65
    # 2. mod 11 gives a nice result set (a distinct number for each solfege)
    x_prime = x % 11
    # 3. map to the solfege offset (e.g. "Do" -> 0, "La" -> 9, ...)
    y = solfege_polynomial(x_prime)

    # combine the solfege offset and the scale to get a [0, 11] number
    # representing the output note
    scale_as_integer += y
    scale_as_integer %= 12

    # use the inverse scale polynomial to get back to our text encoding
    out_note = inverse_scale_polynomial(scale_as_integer)

    # decode back to text
    out_note_human_readable = decode(out_note)
    return out_note_human_readable

def main():
    test_cases = [
        ("C", "Do"),
        ("C", "Re"),
        ("C", "Mi"),
        ("D", "Mi"),
        ("A#", "Fa"),
        ("B", "Do"),
        ("F", "La"),
        ("F", "So"),
        ("D", "Ti"),
    ]

    for case in test_cases:
        scale, solfege = case
        result = note(scale, solfege)
        print(f"note({scale}, {solfege}) = {result}")

if __name__ == "__main__":
    main()
