""" for Python 3"""

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name

    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name

obj = Duck('Howard')
print(obj.name)
obj.name = 'Donald' # inside the setter
print(obj.name)

print(obj.hidden_name)

