class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class LinkedList:
    data = []

    def __init__(self):
        self.first = None

    def append(self, item):
        # This method should append an item to the end of the list
        if self.first is None:
            self.first = item
            self.data.append(item)
            return
        last = self.first
        while True:
            if last.next is None:
                self.data.append(item)
                last.next = item
                break
            last = last.next

    def getLen(self):
        # This method should find the length of the list and return it
        return len(self.data)

    def printAll(self):
        # This method should print all elements in the list from the head to the end
        for item in self.data:
            print(item.data)
