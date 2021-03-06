def checkio(data):

    even = False
    if len(data) % 2 == 0:
        even = True
    # Note: sorted() for not modifying the list and list.sort() for in-place sort
    data.sort()

    if not even:
        print(float(len(data)))
        median_index = int((len(data) / 2.0) - 0.5)
        return data[median_index]
    else:
        # double // for floor division
        # -1 b/c fencepost problem. aka index starts at 0 not 1
        median_index = (len(data) // 2) - 1
        median = (data[median_index] + data[(median_index + 1)]) / 2
        return median

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
