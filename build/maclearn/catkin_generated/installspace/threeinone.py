#!/usr/bin/env python3

import rospy
import message_filters
from geometry_msgs.msg import PoseStamped, TwistStamped, AccelStamped
from custommsg.msg import kinematicstamped

pub = rospy.Publisher('ThreeinOneKinematics', kinematicstamped, queue_size=10)
kinematics = kinematicstamped()

def callback(pose, twist, accel):
	global kinematics
	kinematics.header.stamp = rospy.get_rostime()
	kinematics.pose.position.x = pose.pose.position.x
	kinematics.pose.position.y = pose.pose.position.y
	kinematics.pose.position.z = pose.pose.position.z
	kinematics.pose.orientation.x = pose.pose.orientation.x
	kinematics.pose.orientation.y = pose.pose.orientation.y
	kinematics.pose.orientation.z = pose.pose.orientation.z
	kinematics.pose.orientation.w = pose.pose.orientation.w
	kinematics.twist.linear.x = twist.twist.linear.x
	kinematics.twist.linear.y = twist.twist.linear.y
	kinematics.twist.linear.z = twist.twist.linear.z
	kinematics.twist.angular.x = twist.twist.angular.x
	kinematics.twist.angular.y = twist.twist.angular.y
	kinematics.twist.angular.z = twist.twist.angular.z
	kinematics.accel.linear.x = accel.accel.linear.x
	kinematics.accel.linear.y = accel.accel.linear.y
	kinematics.accel.linear.z = accel.accel.linear.z
	kinematics.accel.angular.x = accel.accel.angular.x
	kinematics.accel.angular.y = accel.accel.angular.y
	kinematics.accel.angular.z = accel.accel.angular.z


def ros_begin():

	rospy.init_node('pose_twist_accel_compiler_node_py', anonymous=True, disable_signals = True)

	sub_vicon_pose = message_filters.Subscriber('/mavros/vision_pose/pose', PoseStamped)
	sub_vicon_twist = message_filters.Subscriber('/vrpn_client_node/flapusp/twist', TwistStamped)
	sub_vicon_accel = message_filters.Subscriber('/vrpn_client_node/flapusp/accel', AccelStamped)

	# synchronize topics
	ts = message_filters.ApproximateTimeSynchronizer([sub_vicon_pose, sub_vicon_twist,sub_vicon_accel], 10000, 0.1, allow_headerless=True)

	# register callback
	ts.registerCallback(callback)

	global kinematics

	rate = rospy.Rate(5) # 10hz
	while not rospy.is_shutdown():
		pub.publish(kinematics)
		rate.sleep()

#if __name__ == "__main__":
ros_begin()
