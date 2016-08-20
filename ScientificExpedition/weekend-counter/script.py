from datetime import date, timedelta


def checkio(from_date, to_date):
    """
        Count the days of rest
    """
    #sat = 5, sun = 6
    date = from_date - to_date
    mydays = abs(date.days)
    sat = sun = (mydays // 7) if (mydays // 7) >= 1 else 0
    leftover = (mydays % 7)

    if leftover > 0:
        newstart = from_date + timedelta(days=((7*sat)))
        while leftover > -1:
            dy_of_wk = newstart.weekday()
            if dy_of_wk == 5:
                sat += 1
            elif dy_of_wk == 6:
                sun += 1
            newstart += timedelta(days=1)
            leftover -= 1
    else:
        if from_date.weekday() == 5:
            sat += 1
        elif from_date.weekday() == 6:
            sun += 1

    return sat + sun
