# duck_simulation/main.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ducks.mallard_duck import MallardDuck
from ducks.model_duck import ModelDuck
from ducks.rubber_duck import RubberDuck
from behaviors.fly_behaviors.fly_rocket_powered import FlyRocketPowered

def main():
    mallard = MallardDuck()
    mallard.display()
    mallard.perform_quack()
    mallard.perform_fly()
    mallard.swim()

    model_duck = ModelDuck()
    model_duck.display()
    model_duck.perform_quack()
    model_duck.perform_fly()
    model_duck.swim()
    
    rubber_duck = RubberDuck()
    rubber_duck.display()
    rubber_duck.perform_quack()
    rubber_duck.perform_fly()
    rubber_duck.swim()
    
    model_duck.set_fly_behavior(FlyRocketPowered())
    model_duck.perform_fly()

if __name__ == "__main__":
    main()
