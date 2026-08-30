#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def doMsg(msg):
    rospy.loginfo("我订阅的数据：%s",msg.data)

if __name__ == "__main__" :
    rospy.init_node("bb")

    sub = rospy.Subscriber("hello",String,doMsg,queue_size = 10)

    rospy.spin()