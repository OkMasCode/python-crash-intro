class robot:
    def __init__(self, name, battery_level = 80):
        self.name = name
        self.battery_level = battery_level
    def __str__(self):
        return f"name: {self.name}. battery level: {self.battery_level}"
    def charge_battery(self):
        self.battery_level += 10
    def move_forward(self):
        if self.battery_level >= 5:
            self.battery_level -= 5
        else:
            print("Battery is too low to move forward")

class flying_robot(robot):
    def __init__(self, name, battery_level=80):
        super().__init__(name, battery_level)
    def fly(self):
        if self.battery_level >= 20:
            self.battery_level -= 20
        else:
            print("Battery level is too low to fly")
    def move_forward(self):
        print(f"{self.name} can't walk, but it's hovering forward!")

class robot2:
    def __init__(self, name, battery_level = 80):
        self.name = name
        self.__battery_level = battery_level
    def __str__(self):
        return f"name: {self.name}. battery level: {self.getter_battery()}"
    def setter_battery(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print("the value is not admissible")
    def getter_battery(self):
        return self.__battery_level
    def charge_battery(self):
        self.setter_battery(self.getter_battery() + 10)
    def move_forward(self):
        if self.getter_battery() >= 5:
            self.setter_battery(self.getter_battery() - 5)
        else:
            print("Battery is too low to move forward")
    
class robot3:
    def __init__(self, name, battery_level = 80):
        self.name = name
        self.battery_level = battery_level
    def __str__(self):
        return f"name: {self.name}. battery level: {self.battery_level}"
    def status(self):
        print("name: ", self.name, ". battery level:", self.battery_level)
    def charge_battery(self):
        self.battery_level += 10
    def move_forward(self):
        if self.battery_level >= 5:
            self.battery_level -= 5
        else:
            print("Battery is too low to move forward")

class Grobot(robot3):
    def __init__(self, name, battery_level=80):
        super().__init__(name, battery_level)
    def status(self):
        print("Ground robot", self.name, "is rolling on the ground")

class Wrobot(robot3):
    def __init__(self, name, battery_level=80):
        super().__init__(name, battery_level)
    def status(self):
        print("Water robot", self.name, "is swimming in the water")

robot1 = robot2("GroundBot")
robot1.move_forward()

robot_list = [Grobot("Gbot 1"),
              Wrobot("Wbot 1"),
              Grobot("Gbot 2"),
              Wrobot("Wbot 2")]
#drone1 = flying_robot("DroneX")
#drone1.fly()
#drone1.move_forward()
#print(drone1)
print(robot1)

for i in robot_list:
    i.status()