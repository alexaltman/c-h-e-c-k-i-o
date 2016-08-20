def checkio(first, second):
    first_list = first.split(",")
    first_list = [x.lower() for x in first_list]

    second_list = second.split(",")
    second_list = [x.lower() for x in second_list]

    third_list = []

    for i in first_list:
        if i in second_list:
            third_list.append(i)

    third_list.sort()
    return ",".join(third_list).strip(",")
