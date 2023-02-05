class ReverseList:
    def __init__(self, contents):
        self.contents = contents
    
    def __iter__(self):
        self.n = len(self.contents)
        return self
    
    def __next__(self):
        self.n -= 1
        if self.n < 0:
            raise StopIteration
        return self.contents[self.n]      

my_list = ReverseList([1, 2, 3, 4])

for number in my_list:
    print(number)