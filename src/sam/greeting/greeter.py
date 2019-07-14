'''
Sam's Greeter class
'''

class Greeter:

    def __init__(self, name):
        self.name = name

    def get_message(self):
        return 'Hello %s - nice to meet you!' % self.name

    def greet(self):
        print(self.get_message())
