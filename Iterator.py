my_list=[10,20,30]
my_iter=iter(my_list)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#custom iterator
class countthree:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=3:
            result=self.num
            self.num+=1
            return result
        else:
            raise StopIteration
counter=countthree()
for value in counter:
    print(value)