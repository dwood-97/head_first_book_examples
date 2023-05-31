# duck_simulation/ducks/model_duck.py

from .duck import Duck
from duck_simulation.behaviors.quack_behaviors.quack import Quack
from duck_simulation.behaviors.fly_behaviors.fly_no_way import FlyNoWay

class ModelDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck!")
