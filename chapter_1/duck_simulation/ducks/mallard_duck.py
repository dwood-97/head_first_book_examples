from .duck import Duck
from duck_simulation.behaviors.quack_behaviors.quack import Quack
from duck_simulation.behaviors.fly_behaviors.fly_with_wings import FlyWithWings

class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a Mallard Duck!")