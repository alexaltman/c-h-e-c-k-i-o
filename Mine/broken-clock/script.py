from datetime import timedelta, datetime


def broken_clock(starting_time, wrong_time, error_description):
    FMT = '%H:%M:%S'
    duration = datetime.strptime(wrong_time, FMT) - datetime.strptime(starting_time, FMT)
    starting_time = datetime.strptime(starting_time, FMT)
    wrong_time = datetime.strptime(wrong_time, FMT)

    # errstr --> ['+5', 'seconds', 'at', '10', 'seconds']
    errstr = error_description.split()
    sec_dict = {'second': 1, 'seconds': 1, 'minutes': 60, 'minute': 60, 'hour': 3600, 'hours': 3600}
    adj_amt = int(errstr[0])*sec_dict[errstr[1]]
    adj_freq = int(errstr[3])*sec_dict[errstr[4]]
    rate = adj_amt / adj_freq
    final_clock = ''

    if rate > 0:
        adj_needed = timedelta(seconds=(duration.seconds / (rate + 1)))
        final_clock = starting_time + adj_needed
    elif rate < 0:
        adj_needed = timedelta(seconds=(duration.seconds / (1 - abs(rate))))
        final_clock = starting_time + adj_needed


    return ("%.2d:%.2d:%.2d" % (final_clock.hour, final_clock.minute, final_clock.second))
