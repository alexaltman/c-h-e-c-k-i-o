class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_NS = width_NS
        self.north = south + width_NS
        self.width_WE = width_WE
        self.east = west + width_WE
        self.height = height
        self.mycorners = {}
        self.myarea = 0
        self.myvol = 0

    def corners(self):
        self.mycorners = { "north-west": [self.north, self.west],
                           "north-east": [self.north, self.east],
                           "south-west": [self.south, self.west],
                           "south-east": [self.south, self.east],
                          }
        return self.mycorners

    def area(self):
        self.myarea = self.width_NS * self.width_WE
        return self.myarea

    def volume(self):
        self.myvol = self.width_NS * self.width_WE * self.height
        return self.myvol

    def __repr__(self):
        return "Building(%r, %r, %r, %r, %r)" % (self.south, self.west, self.width_WE, self.width_NS, self.height)
