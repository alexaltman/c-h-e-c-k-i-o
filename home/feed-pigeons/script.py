def checkio(wheat_servings):
    pigeons = 0
    fed_pigeons = 0
    minutes = 0

    while wheat_servings > 0:
        minutes += 1
        pigeons += minutes

        last_fed_pigeons = fed_pigeons
        fed_pigeons, wheat_servings = feed_pigeons(pigeons, wheat_servings)

        if wheat_servings == 0:
            if last_fed_pigeons > fed_pigeons:
                return last_fed_pigeons
            else:
                return fed_pigeons

def feed_pigeons(pigeons, wheat_servings):
    fed_pigeons = 0
    while wheat_servings > 0:
        wheat_servings -= 1
        fed_pigeons += 1
        if wheat_servings == 0 or fed_pigeons == pigeons:
            return fed_pigeons, wheat_servings


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"
