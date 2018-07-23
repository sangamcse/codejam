def checkone(strlen, pos):
    if strlen is 1 or pos is 1 or pos is ((strlen//2)+1):
        return False
    elif pos <= (strlen//2):
        return checkone(strlen//2, pos)
    else:
        return not checkone(strlen//2, strlen-pos+1)

def kth(pos):
    strlen = 0
    while(strlen <= pos):
        strlen = strlen * 2 + 1
    if checkone(strlen, pos):
        return '1'
    return '0'


def main():
    for case in range(int(input())):
        print('Case #{}: {}'.format(case+1, kth(int(input()))))


if __name__ == '__main__':
    main()
