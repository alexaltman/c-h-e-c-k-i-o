def getlines(start, tot_width):
    lines = []
    for i in range(tot_width):
        lines.append([start + i, start + i + 1])
        lines.append([start + 4 * tot_width + i, start + 4 * tot_width + i + 1])
        lines.append([start + 4 * i, start + 4 * i + 4])
        lines.append([start + tot_width + 4 * i, start + tot_width + 4 * i + 4])
    return lines


def checkio(lines_list):
    lines_list = [sorted(i) for i in lines_list]
    lines_list = sorted(lines_list, key=lambda x: min(x))
    count = 0
    for tot_width in range(1, 4):
        for num1 in range(4 - tot_width):
            for num2 in range((4 - tot_width)):
                issquare = True
                lines = getlines(4 * num1 + num2 + 1, tot_width)
                for l in lines:
                    if l not in lines_list:
                        issquare = False
                        break
                if issquare:
                    count += 1
    return count
