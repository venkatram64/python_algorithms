
def move(disk, source, dest, spare):
    if disk == 0:
        print("move", disk, source, dest)
    else:
        move(disk-1, source, spare, dest)
        print("move", disk, source, dest)
        move(disk-1, spare, dest, source)


if __name__ == '__main__':
    move(1, 0, 1, 2)
    #move(2, 0, 1, 2)