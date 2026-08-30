#!/usr/bin/env python3
import rospy
from my_msgs.msg import state

if __name__ == "__main__":
    rospy.init_node("aa")

    pub = rospy.Publisher("hello",state,queue_size = 10)

    i = state()

    i.name = "xiaoshuai"
    i.age = 18
    i.height = 1.82

    rospy.sleep(1.0)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        pub.publish(i)

        rospy.loginfo("详细信息是：%s,%d,%.2f",i.name,i.age,i.height)

        rate.sleep()