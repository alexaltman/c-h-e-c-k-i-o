def days_diff(date1, date2):
    """
        Find absolute diff in days between dates
    """
    from datetime import date
    a = date(date1[0], date1[1], date1[2])
    b = date(date2[0], date2[1], date2[2])
    c = a - b
    return abs((a - b).days)
