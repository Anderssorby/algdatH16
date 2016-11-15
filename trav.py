from sys import stdin

class Record:
    value = None
    next = None
    def __init__(self, value):
        self.value = value
        self.next = None


def search(record, greatest=0):
    if record is None:
        return greatest
    next = record.next
    return search(next, max(record.value, greatest))



def main():
    first = None
    last = None
    for line in stdin:
        penultimate = last
        last = Record(int(line))
        if first is None:
            first = last
        else:
            penultimate.next = last

    print(search(first))


if __name__ == "__main__":
    main()
