
'''
A mega greeting module. Thomas Jence.
Leonardo was here, and daniel, and Kacper
A mega greeting module.
Leonardo was here, and daniel. kieran is the best though.
'''

from sam.greeting.greeter import Greeter as SamGreeter

greeter_list = [
    SamGreeter('Sam')
]

def main():
    for greeter in greeter_list:
        greeter.greet()


if __name__ == '__main__':
    main()

'Rony'
