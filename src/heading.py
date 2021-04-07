import rospy
from scipy.spatial.transform import Rotation
import numpy as np
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32

def callback_custom(data):
    x = data.orientation.x
    y = data.orientation.y
    z = data.orientation.z
    w = data.orientation.w
    # print(x, y, z, w)
    r = Rotation.from_quat([x,y,z,w])
    print(r.as_euler('xyz') * 180 / np.pi)

def heading():
    rospy.init_node('heading', anonymous=True)
    rospy.Subscriber('imu', Imu, callback_custom)
    # pub = rospy.Publisher('heading', Float32, queue_size=10)  
    # pub.publish(head)
    rospy.spin()

if __name__ == '__main__':
    heading()

# var yaw = atan2(2.0*(q.y*q.z + q.w*q.x), q.w*q.w - q.x*q.x - q.y*q.y + q.z*q.z);
# var pitch = asin(-2.0*(q.x*q.z - q.w*q.y));
# var roll = atan2(2.0*(q.x*q.y + q.w*q.z), q.w*q.w + q.x*q.x - q.y*q.y - q.z*q.z);