from collections import deque

class FindDistance:

    def __init__(self):
        self.m = deque([deque([9, 2, 3]), deque([8, 1, 4]), deque([7, 6, 5])])
        self.end = 9

    def __call__(self, first, second):

        while any(self.end < i for i in [first, second]):
            self.add_layer()

        return self.finddist(first, second)

    def add_layer(self):
        l = len(self.m)
        newend = (l+2)**2
        nums = deque(r for r in range(self.end+1, newend+1)) # 10, 11, 12, ... 25

        self.m.appendleft(deque(i() for i in [nums.pop] + [nums.popleft]*(l+1)))

        for e, row in enumerate(self.m):
            if e == 0:
                continue
            row.appendleft(nums.pop())
            row.append(nums.popleft())
            self.m[e] = row

        self.m.append(deque(i for i in reversed(nums)))

        self.end = newend

    def finddist(self, first, second):
        f_loc = s_loc = ()
        for y, row in enumerate(self.m):
            for x, i in enumerate(row):
                if i == first:
                    f_loc = (y, x)
                elif i == second:
                    s_loc = (y, x)

        return abs(f_loc[0] - s_loc[0]) + abs(f_loc[1] - s_loc[1])


find_distance = FindDistance()
