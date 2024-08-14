tests = [
    ["v1.9", "v1.10", "v1.2", "v1.21", "v1.11", "v1.3"],
    ["Chapter 1", "Chapter 10", "Chapter 2", "Chapter 11", "Chapter 20", "Chapter 3"],
    ["192.168.1.1", "192.168.1.10", "192.168.1.2", "192.168.1.20", "192.168.1.3"],
    ["file1.txt", "file10.txt", "file2.txt", "file20.txt", "file11.txt", "file3.txt"],
    ["estimate-all-history-counts.xlsx", "estimate-cost-price-helper-sheet.xlsx", "estimate-stats(1).xlsx", "estimate-stats.xlsx"],
]

def compare_fn(a, b):
    for a_i, b_i in zip(a, b):
        if a_i > b_i:
            return 1
        elif a_i < b_i:
            return -1
    
    # longer items are ordered later
    if len(a_i) > len(b_i):
        return 1
    elif len(b_i) > len(a_i):
        return -1

    # the items are ordered equivalently
    return 0

def split_item(s):
    # split item into numeric and non-numeric sections, preserving internal order
    # there's probably a nice regex way to do this e.g. with ([^0-9]*)([0-9]*)*
    NUMBERS = "012346789"

    split = []
    subitem = ''
    is_number = False

    for ch in s:
        if is_number is True and ch not in NUMBERS:
            split.append(int(subitem))
            subitem = ''
        elif is_number is False and ch in NUMBERS:
            split.append(subitem)
            subitem = ''

        is_number = ch in NUMBERS
        subitem += ch

    # this should be a do-while or something
    if is_number:
        split.append(int(subitem))
    else:
        split.append(subitem)

    return split


def natural_sort(l):
    # for each item in l,
    #   split item into numeric and non-numeric sections, preserving internal order
    #   (e.g. "v1.9" -> ["v", 1, ".", 9] )
    # 
    # use a basic sort algorithm, but the comparison operator is
    # to compare each element of the split item with each correspondingly
    # positioned element of the other, and if at any point the subitem comparison
    # is nonzero, that determines the overall comparison
    pass


