def my_range(start, end):
    i = start
    while i < end:
        yield i
        i += 1


for number in my_range(1, 5):
    print(number)
    
print("Done")