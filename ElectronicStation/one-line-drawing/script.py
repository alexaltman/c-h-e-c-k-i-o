from collections import Counter

def draw(segments):

    segs = segments.copy()
    verts = []
    c = Counter()
    for seg in segs:
        x1, y1, x2, y2 = seg
        verts.append((x1, y1))
        c[(x1, y1)] += 1
        verts.append((x2, y2))
        c[(x2, y2)] += 1

    odd = 0
    odd1 = ()
    odd2 = ()
    ev = ()
    for k, v in c.items():
        if v % 2 != 0:
            # Get value to start from
            if not odd1:
                odd1 = k
            elif not odd2:
                odd2 = k
            else:
                return []
            # Clean up Vertices.
            if v == 1:
                continue
            elif v == 3:
                verts.remove(k)
            elif v > 3:
                v = v-1
                for i in range(0, v//2):
                    verts.remove(k)
        else:
            if not ev:
                ev = k
            for i in range(0, v//2):
                verts.remove(k)

    if odd1 and not odd2:
        return []

    def findnei(vertex):
        degs = 0
        myseg = ()
        for i in segs:
            x1, y1, x2, y2 = i
            if vertex == (x1, y1):
                if not myseg:
                    myseg = i
                elif c[(x1, y1)] > degs:
                    myseg = i
            elif vertex == (x2, y2):
                if not myseg:
                    myseg = i
                elif c[(x2, y2)] > degs:
                    myseg = i
        return myseg

    if odd1:
        current = odd1
    else:
        current = ev

    path = [current]
    while verts and segs:
        try:
            x1, y1, x2, y2 = findnei(current)
        except TypeError:
            break
        segs.remove((x1, y1, x2, y2))
        verts.remove(current)
        if current == (x1, y1):
            path.append((x2,y2))
            current = (x2,y2)
        elif current == (x2, y2):
            path.append((x1,y1))
            current = (x1,y1)

    return path
