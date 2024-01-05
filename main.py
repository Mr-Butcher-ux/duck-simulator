#Ducks can swim, fly, and quack. Rubber ducks can squick and swim but cannot fly.
# Decoy ducks cannot fly, swim, and quack. Each type of duck flies and quacks differently. ex)
# you can just print out "fly with a wing" or "quack".

#This is the class duck,in this class is defined the actions of the ducks
class Duck(object):
    def __init__(self):
        pass

    def set_fly(self, fb):
        self.fly_behavior = fb

    def set_quack(self, qb):
        self.quack_behavior = qb

    def set_swin(self, sb):
        self.swin_behavior = sb

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def perform_swin(self):
        self.swin_behavior.swin()

#This is the class for the real duck
class RealDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        fly_instance = Fly()
        self.set_fly(fly_instance)
        quack_instance = Quack()
        self.set_quack(quack_instance)
        swin_instance = Swin()
        self.set_swin(swin_instance)
        print("Hello, I am a Real Duck")

#This is the class for the rubber duck
class RubberDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        not_fly_instance = NotFly()
        self.set_fly(not_fly_instance)
        squeak_instance = Squeak()
        self.set_quack(squeak_instance)
        swin_instance = Swin()
        self.set_swin(swin_instance)
        print("Hello, I am a Rubber Duck")

#This is the class for the decoy duck
class DecoyDuck(Duck):
    def __init__(self):
        Duck.__init__(self)
        not_fly_instance = NotFly()
        self.set_fly(not_fly_instance)
        mute_instance = MuteQuack()
        self.set_quack(mute_instance)
        not_swin_instance = NotSwin()
        self.set_swin(not_swin_instance)
        print("Hello, I am a Decoy Duck")


# These are the fly behavior interface and behavior implementation classes.
class FlyBehavior():
    def __init__(self):
        pass

class Fly(FlyBehavior):
    def fly(self):
        print("I can fly.")

class NotFly(FlyBehavior):
    def fly(self):
        print("I can not fly.")



#These are the quack behavior interfaces and behavior implementation classes.
class QuackBehavior():
    def __init__(self):
        pass

class Quack(QuackBehavior):
    def quack(self):
        print("I can quack.")

class MuteQuack(QuackBehavior):
    def quack(self):
        print("I can not quack or squeak.")

class Squeak(QuackBehavior):
    def quack(self):
        print("I can squeak.")

#These are the Swin behavior interface and behavior implementation classes.
class SwinBehavior():
    def __init__(self):
        pass

class Swin(SwinBehavior):
    def swin(self):
        print("I can swin.")

class NotSwin(SwinBehavior):
    def swin(self):
        print("I can not swin.")




#This is the main method or class
if __name__ == "__main__":


    print("\n")
    print("The real duck says: ")
    real = RealDuck()
    real.perform_fly()
    real.perform_swin()
    real.perform_quack()

    print("\n")
    print("The rubber duck says: ")
    rubber = RubberDuck()
    rubber.perform_fly()
    rubber.perform_swin()
    rubber.perform_quack()

    print("\n")
    print("The decoy duck says: ")
    decoy = DecoyDuck()
    decoy.perform_fly()
    decoy.perform_swin()
    decoy.perform_quack()
