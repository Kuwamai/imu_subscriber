#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu

def recv_imu(data):
     data.linear_acceleration


if __name__ == '__main__':
    rospy.init_node('imu_subscriber')
    rospy.Subscriber("imu/data_raw", Imu, recv_imu)
    rospy.spin()
