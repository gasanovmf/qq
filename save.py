path = []

def put(value):
    global path
    path.append(value)


def getPath(field):
    global path
    return list(map(lambda el: el[field], path))