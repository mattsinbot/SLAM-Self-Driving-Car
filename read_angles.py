import rospy
import baxter_interface

# Initialize ROS node
rospy.init_node('myplan_executer')

# Select limb side
work_limb = 'left'
limb = baxter_interface.Limb(work_limb)

# Acquire current joint angles
current_angles = limb.joint_angles()

# Read joint angle file
data = open('joint_angles1.txt', 'r')
for i in range(10):
    line = data.readline()
    angles = line.split(",")
    # Set joint angles
    current_angles[work_limb + "_s0"] = float(angles[0])
    current_angles[work_limb + "_s1"] = float(angles[1])
    current_angles[work_limb + "_e0"] = float(angles[2])
    current_angles[work_limb + "_e1"] = float(angles[3])
    current_angles[work_limb + "_w0"] = float(angles[4])
    current_angles[work_limb + "_w1"] = float(angles[5])
    current_angles[work_limb + "_w2"] = float(angles[6])
    # Execute
    limb.move_to_joint_positions(current_angles)
    print(current_angles)
