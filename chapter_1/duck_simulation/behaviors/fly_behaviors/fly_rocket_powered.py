# duck_simulation/behaviors/fly_behaviors/fly_rocket_powered.py

from .fly_behavior import FlyBehavior

class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")
