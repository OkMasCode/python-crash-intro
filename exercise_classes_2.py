import random

class battery:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.level = capacity
    
    def drain(self, ammount):
        self.level = max(0, self.level-ammount)
        print(f"the battery level is: {self.level}/{self.capacity}")

    def recharge(self):
        self.level = self.capacity
        print("battery recharged to the maximum level ")

class motor:
    def __init__(self, power):
        self.power = power
    
    def move(self, battery):
        battery.drain(self.power)
    
class robot:
    def __init__(self, name):
        self.name = name
        self.battery = battery()
        self.motor1 = motor(5)
        self.motor2 = motor(5)

    def move_forward(self):
        self.motor1.move(self.battery)
        self.motor1.move(self.battery)
        print(f"the robot has moved forward, the battery level is now {self.battery.level}/{self.battery.capacity}")


turtle1 = robot("turtle")
turtle1.move_forward()
turtle1.move_forward()
turtle1.battery.recharge()
turtle1.move_forward()

class sensor:
    def __init__(self):
        return None

    def read_value(self):
        dummy_sensor_value = 0
        return dummy_sensor_value
    
class tempsensor(sensor):

    def read_value(self):
        return random.randint(-10, 40)

class distsensor(sensor):

    def read_value(self):
        return random.randint(0, 100)  

class robot2:
    def __init__(self, name):
        self.name = name
        self.sensors = []
    
    def add_sensors(self, sensor):
        self.sensors.append(sensor)

    def read_sensors(self):
        for x in self.sensors:
            value = x.read_value()
            print("The value read by the sensor is ", value)

turtle2 = robot2("turtle2")
sens1 = tempsensor()
turtle2.add_sensors(sens1)
sens2 = tempsensor()
turtle2.add_sensors(sens1)
sens3 = distsensor()
turtle2.add_sensors(sens1)
sens4 = distsensor()
turtle2.add_sensors(sens1)

turtle2.read_sensors()


