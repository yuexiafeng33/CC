#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

if __name__ == "__main__":
    rospy.init_node("cc")

    pub = rospy.Publisher("hello", String, queue_size=10)

    msg = String()
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        msg.data = "cc"
        pub.publish(msg)
        rate.sleep()