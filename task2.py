class TV:
    def on(self):
        print("on")

class Speaker:
    def on(self):
        print("on")

class Light:
    def on(self):
        print("on")



class Facade:
    def __init__(self):
        self.light = Light()
        self.tv = TV()
        self.speaker = Speaker()


    def start(self):
        self.light.on()
        self.speaker.on()
        self.tv.on()

facade = Facade()
facade.start()