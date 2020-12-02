data = []
with open('input.txt') as f:
    for l in f:
        data.append(l)

def Part1():
    validPasswords = 0
    for l in data:
        line = l.split(': ')
        reqs = line[0].split(' ')
        occs = reqs[0].split('-')
        minOccs = int(occs[0])
        maxOccs= int(occs[1])
        char = reqs[1]
        Obvs = line[1].count(char)
        if Obvs >= minOccs and Obvs <= maxOccs:
            validPasswords += 1
    return validPasswords  

def Part2():
    validPasswords = 0
    # data = ['1-3 a: abcde', '1-3 b: cdefg', '2-9 c: 123456789']

    for l in data:
        criteria, password = l.split(': ')
        firstPosition, lastPosition, character = criteria.replace('-',' ').split(' ')
        print (','.join(x for x in [firstPosition, lastPosition, character, password]))
        if password[int(firstPosition)-1] == character and password[int(lastPosition)-1] == character:
            pass
        elif password[int(firstPosition)-1] == character or password[int(lastPosition)-1] == character:
            validPasswords += 1

    print(validPasswords)


def main():
    # print(Part1())
    Part2()

if __name__ == '__main__':
    main()