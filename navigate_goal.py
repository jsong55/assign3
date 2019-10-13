#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

def move_to_goal(xGoal, yGoal):

	ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

	while(not ac.wait_for_server(rospy.Ducation.from_sec(5))):
		rospy.loginfo("Waiting for the move_base action server to come up")

	goal = MoveBaseGoal()

	goal.target_pose.header.frame_id = "map"
	goal.target_pose.header.stamp = rospy.Time.now()

	# moving towards the goal */
	goal.target_pose.pose.position = Point(xGoal,yGoal,0)

	#or
	#goal.target_pose.pose.position.x = xGoal
	#goal.target_pose.pose.position.y = yGoal
	#goal.target_pose.pose.position.z = 0

	goal.target_pose.pose.orientation.x = 0.0
	goal.target_pose.pose.orientation.y = 0.0
	goal.target_pose.pose.orientation.z = 0.0
	goal.target_pose.pose.orientation.w = 1.0

	rospy.loginfo("Sending goal location ...")
	ac.send_goal(goal)

	ac.wait_for_result(rospy.Duration(69))

	if(ac.get_state() == GoalStatus.SUCCEEDED):
		rospy.loginfo("Reached the destination")
		return True
	else:
		rospy.loginfo("Failed to reach")
		return False

if __name__ == '__main__':
	rospy.init_node('map_navigation', anonymous = False)
	x_goal = -2.124123124
	y_goal = 4.021231254123
	print'start go to goal'
	move_to_goal(x_goal,y_goal)
	rospy.spin()