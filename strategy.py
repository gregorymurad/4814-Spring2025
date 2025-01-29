"""
The SimUDuck App - Strategy Design Pattern

Joe works for a company that makes a highly successful duck
pond simulation game, SimUDuck. The game can show a large
variety of duck species swimming and making quacking sounds.
"""

###############################################################################
# Ducks
###############################################################################

# Abstract class Duck
class Duck:
    fly_behavior = None
    quack_behavior = None

    def display(self):
        pass

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    # TODO: write the set_quack_behavior method
    def set_quack_behavior(self,new_quack_behavior):
        self.quack_behavior = new_quack_behavior

    # TODO: write the set_fly_behavior method
    def set_fly_behavior(self, new_fly_behavior):
        self.fly_behavior = new_fly_behavior
    def swim(self):
        print("All ducks float, even decoys!!")

class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")

class DecoyDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a decoy duck")

class RubberDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a cute rubber duck")

class RedHeadDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a red-headed duck and I can dive")

# TODO: write the ModelDuck class

###############################################################################
# Quack behaviors
###############################################################################

class QuackBehavior:
    def quack(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("Quack")

# TODO: write the MuteQuack class
class MuteQuack(QuackBehavior):
    def quack(self):
        print("**SILENCE**")

# TODO: write the Squeak class
class Squeak(QuackBehavior):
    def quack(self):
        print("SqUeAk")

# TODO: write the FakeQuack class
class FakeQuack(QuackBehavior):
    def quack(self):
        print("Quak")

###############################################################################
# Fly behaviors
###############################################################################
class FlyBehavior():
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


# TODO: write the FlyNoWay class
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I cannot fly 😔")


# TODO: write the FlyRocketPowered class
class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I can fly super fast 🚀")

if __name__ == '__main__':
    # TODO: instantiate an object of MallardDuck
    mallard1 = MallardDuck()
    mallard1.display()
    mallard1.quack()
    mallard1.swim()

    # TODO: instantiate an object of RedHeadDuck
    redheadduck1 = RedHeadDuck()
    redheadduck1.display()
    redheadduck1.quack()
    redheadduck1.swim()

    rubber1 = RubberDuck()
    rubber1.quack()
    rubber1.set_quack_behavior(FakeQuack())
    rubber1.quack()

"""
References:
This lecture was designed by Dr Gregory Reis based on the book
Elisabeth Freeman, Eric Freeman, Bert Bates, and Kathy Sierra. 2004
Head First Design Patterns. O' Reilly & Associates, Inc.,
Dr Kip Irvine's class notes, and using the simuduck.py written
by Miguel Alba and modified by Dr Gregory Reis
"""