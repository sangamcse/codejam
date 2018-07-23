def countbus():
    no_of_bus = int(input())
    pair = {}
    buses = [int(bus) for bus in input().split()]
    for _ in range(no_of_bus):
        pair[_] = [buses[2*_], buses[(2*_)+1]]
    msg = []
    for _ in range(int(input())):
        query = int(input())
        count = 0
        for i, city in pair.items():
            if(query>=city[0] and query<=city[1]):
                count = count+1
        msg.append(str(count))
    i = input()
    return ' '.join(msg)


def main():
    for _ in range(int(input())):
        print('Case #{}: {}'.format(_+1, countbus()))


if __name__ == '__main__':
    main()
