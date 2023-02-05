class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value - other.value)

    def __repr__(self):
        return f"Number({self.value})"


result = Number(5) + Number(3)
print(result)