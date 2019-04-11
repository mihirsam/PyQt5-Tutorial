class test:
    def __init__(self):
        self.hello()

    def hello(self):
        print("tthis is hellow!")
        self.okay("okay")

    def okay(self, message):
        print(message)


Test = test()
