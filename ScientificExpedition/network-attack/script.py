def capture(m):
    minutes = -1
    infected = [0]

    connected = whoisconnected(0, m)
    while len(infected) != len(m):
        for computer in connected:
            if computer in infected:
                continue
            elif computer[1] > 0:
                computer[1] -= 1
            else:
                infected.append(computer)
                new_conns = whoisconnected(computer[0], m)
                # how to to tell if new conns add time?
                connected.extend([j for j in new_conns if j not in connected])
        minutes += 1
    return minutes

def whoisconnected(computer, m):
    connected = []
    for i in range(1, len(m)):
        if m[computer][i] == m[i][computer] == 1:
            # appending comp #, then sec lvl
            connected.append([i, m[i][i]])
    return connected
