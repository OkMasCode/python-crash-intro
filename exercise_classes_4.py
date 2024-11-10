class Joint:
    def __init__(self, joint_id, current_angle, min_angle = 0, max_angle = 360):
        self.joint_id = joint_id
        self.current_angle = current_angle
        self.min_angle = min_angle
        self.max_angle = max_angle

    def get_current_angle(self):
        return self.current_angle
    
    def new_angle(self, new_angle):
        if new_angle >= self.min_angle and new_angle < self.max_angle:
            self.current_angle = new_angle
        else:
            print("The position of the joint cannot be reached")
    
class RobotArm:
    def __init__(self, name):
        self.name = name
        self.joints = []

    def add_joint(self, joint):
        self.joints.append(joint)

    def move_all_joints(self, angles):
        if len(angles) <= len(self.joints):
            for x in range(len(angles)):
                self.joints[x].new_angle(angles[x])
        else:
            for x in range(len(self.joints)):
                self.joints[x].new_angle(angles[x]) 

    def print_position(self):
        i = 0
        for x in self.joints:
            i += 1
            print(f"Position of {x.joint_id}: {x.get_current_angle()}")     

joint0 = Joint("Joint0", 0, 0, 180)
joint1 = Joint("Joint1", 20, 0, 360)
joint2 = Joint("Joint2", 20, 0, 360)
joint3 = Joint("Joint3", 0, 0, 90)

manipulator = RobotArm("manipulator")
manipulator.add_joint(joint0)
manipulator.add_joint(joint1)
manipulator.add_joint(joint2)
manipulator.add_joint(joint3)

manipulator.print_position()

angles = [90, 90, 90, 45]
angles2 = [45, 0, 20]
angles3 = [380, 32, 400, 100]

manipulator.move_all_joints(angles)
manipulator.print_position()

manipulator.move_all_joints(angles2)
manipulator.print_position()

manipulator.move_all_joints(angles3)
manipulator.print_position()
