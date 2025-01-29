# Example 1

class Car:
    def __init__(self,x,y):
        self.color = x
        self.maker = y

    def start_engine(self):
        print("Engine started.")

    def stop_engine(self):
        print("Engine stopped.")

myCar = Car("white","Hyundai")
print(myCar)

print(myCar.maker,myCar.color)
myCar.start_engine()
myCar.stop_engine()

# Example 2

class FIUStudent:
    minimum_grade = 93
    def __init__(self,first_name,last_name,pid,email,grade):
        self.first_name = first_name
        self.last_name = last_name
        self.pid = pid
        self.email = email
        self.grade = grade

    def current_grade(self):
        return f"{self.first_name}\'s current grade is {self.grade}."

andreB = FIUStudent("Andre","Brito",123,"andre@fiu.edu",83)
dannyR = FIUStudent("Daniel","Ruiz",234,"daniel@fiu.edu",93)

print(andreB.current_grade())
print(dannyR.current_grade())

class UniversityPerson:
    def __init__(self,name,pid):
        self.personName = name
        self.pantherID = pid

    def get_name(self):
        print(f"FIU\'s person name is {self.personName}")

class Faculty(UniversityPerson):
    def __init__(self,name,pid,department):
        super().__init__(name,pid) # it calls the init function of the parent class
        self.department = department

# TODO: Create a Student class with exclusive property major

class Student(UniversityPerson):
    def __init__(self,name,pid,major):
        super().__init__(name,pid)
        self.major = major

class Robot:
    def __init__(self,name,weight,battery_life,price):
        self.name = name
        self.weight = weight
        self.battery_life = battery_life
        self.price = price
    def move(self):
        return "I am moving."
class AquaticRobot(Robot):
    def __init__(self,name,weight,battery_life,price,sensors,motors,autonomy):
        super().__init__(name,weight,battery_life,price)
        self.sensors = sensors
        self.motors = motors
        self.autonomy = autonomy
    def move(self):
        return "I can swim faster than a shark."

robot1 = Robot("zig",100,2,499.99)
robot2 = AquaticRobot("ecomapper",4000,8,200000,["depth","temperature"],4,True)
print(robot1.move())
print(robot2.move())

### INTERFACES

from abc import abstractmethod, ABC

class StreamingService(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def add_subscriber(self, username):
        pass

    @abstractmethod
    def remove_subscriber(self,username):
        pass

    def display(self):
        return "I am the greatest streaming service ever"


class VideoStreaming(StreamingService):
    def __init__(self,name,cost,subscribers):
        self.name = name
        self.cost = cost
        self.subscribers = subscribers

    def play(self):
        print("I am an American streaming service and production company")

    def add_subscriber(self, username):
        self.subscribers.append(username)

    def remove_subscriber(self,username):
        self.subscribers.remove(username)

    def display(self):
        return "I provide the best tv shows and movies to my subscribers"

netflix = VideoStreaming("Netflix",30,[])
netflix.add_subscriber("greg")
print(netflix.subscribers)