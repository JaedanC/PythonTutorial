class NormalIter:
    def ready(self, contents):
        self.contents = contents
        self.n = 0

    def __next__(self):
        if self.n < len(self.contents):
            element = self.contents[self.n]
            self.n += 1
            return element
        raise StopIteration

class ReverseIter:
    def ready(self, contents):
        self.contents = contents
        self.n = len(self.contents) - 1

    def __next__(self):
        if self.n >= 0:
            element = self.contents[self.n]
            self.n -= 1
            return element
        raise StopIteration

class MyList:
    def __init__(self, contents, iterator):
        self.contents = contents
        self.iterator = iterator
    
    def __iter__(self):
        self.iterator.ready(self.contents)
        return self.iterator

forwards = MyList([1, 2, 3, 4], NormalIter())
backwards = MyList([1, 2, 3, 4], ReverseIter())

print("Forwards")
for num in forwards:
    print(num)

print("Backwards")
for num in backwards:
    print(num)