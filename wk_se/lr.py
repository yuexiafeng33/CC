#!/usr/bin/env python3
import rospy
from my_msgs.msg import state

def doMsg(i):
    rospy.loginfo("我订阅的数据：%s,%d,%.2f",i.name,i.age,i.height)

if __name__ == "__main__":
    rospy.init_node("dd")

    sub = rospy.Subscriber("hello",state,doMsg,queue_size = 10)

    rospy.spin()