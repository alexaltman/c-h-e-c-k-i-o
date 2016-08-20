from itertools import chain

def find_cycle(cons):
    allpaths = {i:[] for i in chain.from_iterable(cons)}
    [allpaths[i].append(con) for i in allpaths.keys() for con in cons if i in con]

    cycles = []

    def getpaths(node, seen):
        seen_nodes = list(chain.from_iterable(seen))
        #paths = [con for con in cons if node in con and con not in seen]
        relevant_paths = []
        for path in allpaths[node]:
            if path not in seen:
                newnode = path[1] if path[0] == node else path[0]
                if seen_nodes.count(node) < 2 and seen_nodes.count(newnode) < 2:
                    relevant_paths.append(path)
        return relevant_paths

    def followcycle(node, seen):
        paths = getpaths(node, seen)
        for path in paths:
            newnode = path[1] if path[1] != node else path[0]
            mycycle = followcycle(newnode, seen + [path])
            if len(mycycle) > 2:
                if mycycle[0][0] == mycycle[-1][1] or mycycle[0][0] == mycycle[-1][0]:
                    cycles.append(mycycle)
        return seen

    for node in allpaths.keys():
        followcycle(node, [])

    largest = []
    for cycle in cycles:
        if len(cycle) > len(largest):
            largest = cycle

    myl = []
    [myl.append(x) for i in largest for x in i if x not in myl]
    return myl + [myl[0]] if len(myl) else []
