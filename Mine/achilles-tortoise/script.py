def chase(a1_speed, t2_speed, advantage):
    x = (t2_speed * advantage) / (a1_speed-t2_speed)
    return x + advantage
