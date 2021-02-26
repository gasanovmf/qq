
class Saver:

    def __init__(self):
        self.path = []

    def put(self, value):
        self.path.append(value)


    def getPath(self, field):
        return list(map(lambda el: el[field], self.path))