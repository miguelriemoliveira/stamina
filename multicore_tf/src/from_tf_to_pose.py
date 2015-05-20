#!/usr/bin/env python  

import roslib
import rospy
import math
import tf
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped
from tf.transformations import euler_from_quaternion

if __name__ == '__main__':
    rospy.init_node('from_tf_to_pose')

    pub = rospy.Publisher('/pose_map_to_np', geometry_msgs.msg.PoseStamped, queue_size=10)

    listener = tf.TransformListener()

    br = tf.TransformBroadcaster()
    rate = rospy.Rate(50)

    rospy.sleep(1)

    while not rospy.is_shutdown(): 

        rate.sleep()
        try:
            now = rospy.Time.now()
            #listener.waitForTransform("/map", "/np", now, rospy.Duration(1.0))
            now = listener.getLatestCommonTime("/map", "/np")
            (trans,rot) = listener.lookupTransform('/map', '/np', now)
            #angles = euler_from_quaternion(rot)

            pose = geometry_msgs.msg.PoseStamped()
            pose.header.frame_id = "/map"
            #TODO should be the time of the transform
            #pose.header.stamp = rospy.get_rostime()
            pose.header.stamp = now
            pose.pose.position.x = trans[0]
            pose.pose.position.y = trans[1]
            pose.pose.position.z = trans[2]
            pose.pose.orientation.x = rot[0]
            pose.pose.orientation.y = rot[1]
            pose.pose.orientation.z = rot[2]
            pose.pose.orientation.w = rot[3]
            pub.publish(pose)

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            rospy.loginfo("Could no get transform from /map to /np")
    


