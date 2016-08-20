def checkio(number):

    bin_num = bin(number)
    count = 0
    for i in str(bin_num):
        if i == "1":
            count += 1
    return count
