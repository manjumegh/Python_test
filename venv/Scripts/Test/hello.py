import sys
import os

class Hello:
    def __init__(self, name):
        self.name = name

    def printName(self):
        print(f'hello world {self.name}')

if __name__ == "__main__":
    hello = Hello('manju')
    hello.printName()