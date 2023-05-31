# duck_simulation/ducks/rubber_duck.py

from .duck import Duck
from duck_simulation.behaviors.quack_behaviors.squeak import Squeak
from duck_simulation.behaviors.fly_behaviors.fly_no_way import FlyNoWay

class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.quack_behavior = Squeak()
        self.fly_behavior = FlyNoWay()

    def display(self):
        print("I'm a rubber duck!")
