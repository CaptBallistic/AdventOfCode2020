from functools import reduce

data = []

# with open('test.txt') as f:
with open('input.txt') as f:
    for l in f:
        data.append(l)

def Part1(yIncrement, xIncrement):
    x, y, trees = 0, 0, 0
    while y <= len(data) - 1:
        if data[y][x] == '#':
            trees += 1
        else:
            pass
        x += xIncrement
        x = x%(len(data[y])-1)
        y += yIncrement

    return trees  


def Part2(xIncrement, yIncrement):
    result = []
    i = 0

    while i < len(yIncrement):
        x, y, trees = 0, 0, 0
        while y <= len(data) - 1:
            if data[y][x] == '#':
                trees += 1
            else:
                pass
            x += xIncrement[i]
            x = x%(len(data[y])-1)                
            y += yIncrement[i]

        result.append(trees)
        i += 1
    
    return reduce(lambda x, y: x*y, result)



def main():
    # print(Part1(1, 3))
    print(Part2([1,3,5,7,1], [1,1,1,1,2]))

if __name__ == '__main__':
    main()