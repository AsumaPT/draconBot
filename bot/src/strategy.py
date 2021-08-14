import random
import math

def randomizar(ps):
    pixelStack = random.sample(ps, len(ps))
    return pixelStack

def columns(ps):
    pixelStack = []
    for i in ps:
        if i[0] % 2 == 0:
            pixelStack.append(i)
    for i in ps:
        pixelStack.append(i)

    return pixelStack

def lines(ps):
    pixelStack = []
    for i in ps:
        if i[1] % 2 == 0:
            pixelStack.append(i)
    for i in ps:
        pixelStack.append(i)

    return pixelStack

def checkers(ps):
    pixelStack = []
    vez = 0
    for i in ps:
        if vez == 0:
            pixelStack.append(i)
            vez = 1
        else:
            vez = 0
    
    for i in ps:
        pixelStack.append(i)

    return pixelStack

def diagonal(ps):
    pixelStack = []
    numbers = []
    for i in ps:
        x = i[0]
        y = i[1]
        numbers.append(x+y)

    while len(ps) > 0:
        index = numbers.index(min(numbers))
        pixelStack.append(ps[index])
        numbers.pop(index)
        ps.pop(index)

    return pixelStack


def rightdiagonal(ps):
    pixelStack = []
    numbers = []
    for i in ps:
        x = i[0]
        y = i[1]
        numbers.append(x-y)

    while len(ps) > 0:
        index = numbers.index(max(numbers))
        pixelStack.append(ps[index])
        numbers.pop(index)
        ps.pop(index)

    return pixelStack

def horizontal(ps):
    pixelStack = sorted(ps, key=lambda x: x[0])
    return pixelStack

def spiral(ps, x, y, width, height):
    pixelStack = []

    def spiral(N, M):
        x,y = 0,0
        dx, dy = 0, -1
        out = []
        for _ in range(N*M):
            if abs(x) == abs(y) and [dx,dy] != [1,0] or x>0 and y == 1-x:
                dx, dy = -dy, dx            # corner, change direction
            if abs(x)>N/2 or abs(y)>M/2:    # non-square
                dx, dy = -dy, dx            # change direction
                x, y = -y+dx, x+dy          # jump
            out.append([x, y])
            x, y = x+dx, y+dy
        return out

    start_x = math.trunc((width-1)/2)
    start_y = math.trunc((height-1)/2)
    for a,b in spiral(width, height):
        sx = x+(start_x+a)
        sy = y+(start_y+b)
        for i in ps:
            if i[0] == sx and i[1] == sy:
                pixelStack.append(i)
    return pixelStack

def randomlinear(ps):
    pixelStack = []
    line_random = []
    line = ps[0][1]
    for i in ps:
        line_atual = i[1]
        if line == line_atual:
            line_random.append(i)
        else:
            random.shuffle(line_random)
            pixelStack.extend(line_random)
            line = i[1]
            line_random = []
            line_random.append(i)
    return pixelStack

def circle(ps, x, y, width, height):
    pixelStack = []
    distances = []
    start_x = x+(math.trunc((width-1)/2))
    start_y = y+(math.trunc((height-1)/2))
    for i in ps:
        if i[0] == start_x and i[1] == start_y:
            pixelStack.append(i)
            distances.append(0)
        else: 
            dist = math.sqrt((i[0] - start_x)**2 + (i[1] - start_y)**2)
            distances.append(dist)

    while len(ps) > 0:
        index = distances.index(min(distances))
        pixelStack.append(ps[index])
        distances.pop(index)
        ps.pop(index)

    return pixelStack

def alternativelinear(ps):
    pixelStack = []
    line_random = []
    line = ps[0][1]
    for i in ps:
        line_atual = i[1]
        if line == line_atual:
            line_random.append(i)
        else:
            line_random = line_random if line % 2 == 0 else line_random[::-1]
            pixelStack.extend(line_random)
            line = i[1]
            line_random = []
            line_random.append(i)
    return pixelStack






    




    


