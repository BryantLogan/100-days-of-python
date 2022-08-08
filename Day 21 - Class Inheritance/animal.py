# Class inheritance can be attributes and behaviors

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


# Allows anything in Fish to inherit anything from the Animal class
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")
    
nemo= Fish()

nemo.swim()
nemo.breathe()