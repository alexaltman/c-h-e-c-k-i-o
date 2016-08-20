class Friends:
    def __init__(self, connections):
        self.connections = connections

    def add(self, connection):
        for i in self.connections:
            if i.issubset(connection):
                return False
        self.connections = list(self.connections)
        self.connections.append(connection)
        self.connections = tuple(self.connections)
        return True


    def remove(self, connection):
        for i in self.connections:
            if i.issubset(connection):
                self.connections = list(self.connections)
                self.connections.remove(connection)
                self.connections = tuple(self.connections)
                return True
        return False

    def names(self):
        s = set()
        for i in self.connections:
            s = s.union(i)
        return s

    def connected(self, name):
        s = set()
        for i in self.connections:
            if name in i:
                s = s.union(i)
                s.remove(name)

        if not s:
            return set()
        else:
            return s
