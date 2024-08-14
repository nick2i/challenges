tests = [
    ["v1.9", "v1.10", "v1.2", "v1.21", "v1.11", "v1.3"],
    ["Chapter 1", "Chapter 10", "Chapter 2", "Chapter 11", "Chapter 20", "Chapter 3"],
    ["192.168.1.1", "192.168.1.10", "192.168.1.2", "192.168.1.20", "192.168.1.3"],
    ["file1.txt", "file10.txt", "file2.txt", "file20.txt", "file11.txt", "file3.txt"],
    ["estimate-all-history-counts.xlsx", "estimate-cost-price-helper-sheet.xlsx", "estimate-stats(1).xlsx", "estimate-stats.xlsx"],
]

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
    return sorted(l, key=split_item)

def main():
    sorted_tests = [natural_sort(test) for test in tests]
    for test in tests:
        sorted_test = natural_sort(test)
        #print("Unordered:\t\t\t| Ordered:")
        max_len = max(len(x) for x in test)
        header = "\nUnordered: "
        header += " " * (3 + max_len - len(header))
        header += "| "
        header += "Ordered:"
        print(header)
        for unordered_item, ordered_item in zip(test, sorted_test):
            row_entry = f" {unordered_item} "
            row_entry += " " * (3 + max_len - len(row_entry))
            row_entry += f"|  {ordered_item}"
            print(row_entry)
            #print(f" {unordered_item}\t\t\t|  {ordered_item}")

if __name__ == "__main__":
    main()

