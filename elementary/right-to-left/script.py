def left_join(phrases):

    phrases = list(phrases)
    items = ""
    for i in phrases:
        i = i.replace("right", "left")
        items += (i+ ",")
    return items.strip(",")
