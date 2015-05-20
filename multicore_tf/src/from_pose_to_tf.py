#!/usr/bin/env python  

import roslib
import rospy
import math
import tf
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion

def callback(data):
    br.sendTransform((data.pose.position.x, data.pose.position.y, data.pose.position.z), (data.pose.orientation.x, data.pose.orientation.y, data.pose.orientation.z, data.pose.orientation.w), rospy.Time.now(), "/base_link", "/map")

if __name__ == '__main__':

    rospy.init_node('from_pose_to_tf')
    br = tf.TransformBroadcaster()

    rospy.Subscriber("/pose_map_to_np", PoseStamped, callback)

    rate = rospy.Rate(50)
    while not rospy.is_shutdown(): 
        rate.sleep()
   


