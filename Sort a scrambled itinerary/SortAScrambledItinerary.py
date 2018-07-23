def FindFirst(arrival, destination):
    for destn in destination:
        if destn not in arrival:
            return destn


def sequence(Tickets):
    arrival = {}
    destination = {}
    for ticket in Tickets:
        arrival[ticket[1]] = 0
        destination[ticket[0]] = ticket[1]
    current = FindFirst(arrival, destination)
    msgs = []
    while current in destination:
        next = destination[current]
        msgs.append(current+'-'+next)
        current = next
    return ' '.join(msgs)


def main():
    for i in range(int(input())):
        Tickets = []
        for _ in range(int(input())):
            Tickets.append([input(), input()])
        print('Case #{}: {}'.format((i+1), sequence(Tickets)))


if __name__ == '__main__':
    main()
