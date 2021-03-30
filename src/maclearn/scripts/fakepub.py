#!/usr/bin/env python3
# ros and lib imports
import rospy
import message_filters
from geometry_msgs.msg import PoseStamped, TwistStamped, AccelStamped
from custommsg.msg import ppmchnls

def fakepub():

	rospy.init_node('fakepub_node', anonymous=True, disable_signals = True)

	pub_vicon_pose = rospy.Publisher('/mavros/vision_pose/pose', PoseStamped, queue_size=100000)
	pub_vicon_twist = rospy.Publisher('/vrpn_client_node/flapusp/twist', TwistStamped, queue_size=100000)
	pub_vicon_accel = rospy.Publisher('/vrpn_client_node/flapusp/accel', AccelStamped, queue_size=100000)

	msg_pose = PoseStamped()
	msg_twist = TwistStamped()
	msg_accel = AccelStamped()

	msg_pose.pose.position.x = 67
	msg_twist.twist.linear.y = 6
	msg_accel.accel.linear.z = -8

	rate = rospy.Rate(30)

	while not rospy.is_shutdown():

		msg_pose.header.stamp = rospy.get_rostime()
		msg_twist.header.stamp = rospy.get_rostime()
		msg_accel.header.stamp = rospy.get_rostime()

		pub_vicon_pose.publish(msg_pose)
		pub_vicon_twist.publish(msg_twist)
		pub_vicon_accel.publish(msg_accel)

		rate.sleep()

if __name__ == "__main__":

	fakepub()