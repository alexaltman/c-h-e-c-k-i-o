import calendar

def checkio(year):
    mycal = calendar.Calendar()
    return len([i for m in range(1, 13) for i in mycal.itermonthdays2(year, m) if i[0] if i[1] == 4 if i[0] == 13])
