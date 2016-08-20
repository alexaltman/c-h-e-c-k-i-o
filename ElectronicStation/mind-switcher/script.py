def mind_switcher(journal):

    robots = {}
    reset_seq = []
    chains = []

    def swapit(journal):
        for body1, body2 in journal:
            if body1 not in robots:
                robots[body1] = body1
            if body2 not in robots:
                robots[body2] = body2

            robots[body1], robots[body2] = robots[body2], robots[body1]

    def buildchains(robots):
        allrobots = set(robots.keys())

        while allrobots:
            chains.append([allrobots.pop()])

            while True:
                next = robots[chains[-1][-1]]

                if next == chains[-1][0]:
                    if len(chains[-1]) == 1:
                        chains.pop()
                    break

                chains[-1].append(next)
                allrobots.remove(next)

    def create_reset_seq(chains):
        first = 'nikola'
        second = 'sophia'

        for chain in chains:
            reset_seq.append({first, chain[-1]})

            for body in chain:
                reset_seq.append({second, body})
            reset_seq.append({first, chain[0]})

        if len(chains) % 2 == 1:
            reset_seq.append({first, second})

    swapit(journal)
    buildchains(robots)
    create_reset_seq(chains)

    return reset_seq
