data = []

with open('Day1Input.csv') as f:
    for l in f:
        data.append(int(l))

def Part1():
    for d1 in data:
        for d2 in data:
            if d1 + d2 == 2020:
                return(d1 * d2)

def Part2():
    for d1 in data:
        for d2 in data:
            for d3 in data:
                if d1 + d2 + d3 == 2020:
                    return (d1 * d2 * d3)

def main():
    print(Part1())
    print(Part2())

if __name__ == '__main__':
    main()