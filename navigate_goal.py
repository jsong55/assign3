#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

def move_to_goal(xGoal, yGoal):

	ac = actionlib.SimpleActionClient("move_base", MoveBaseAction)

	while(not ac.wait_for_server(rospy.Duration.from_sec(5))):
		rospy.loginfo("Waiting for the move_base action server to come up")

	goal = MoveBaseGoal()

	goal.target_pose.header.frame_id = "map"
	goal.target_pose.header.stamp = rospy.Time.now()

	# moving towards the goal */
	goal.target_pose.pose.position = Point(xGoal,yGoal,0)

	
	goal.target_pose.pose.position.x = xGoal
	goal.target_pose.pose.position.y = yGoal
	goal.target_pose.pose.position.z = 0

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

	waypoint = input("Let's go to a position from 1-5, 1 is bottom-left, 2 is the top-left, 3 is top-right, 4 is bottom-right, 5 is going outside the room:::: ")
	if (waypoint == 1):
		x_goal = -1.2
		y_goal = 4.7
	elif (waypoint == 2):
		x_goal = -2.62
		y_goal = 10.49
	elif (waypoint == 3):
		x_goal = 2.05
		y_goal = 10.965
	elif (waypoint == 4):
		x_goal = 2.79
		y_goal = 5.163
	elif (waypoint == 5):
		x_goal = -2.21266
		y_goal = 11.02927
		rospy.sleep(2)
		x_goal = -2.7870
		y_goal = 13.5307
	else: 
		print'unknown waypoint, try again'

	print'start go to goal'
	move_to_goal(x_goal,y_goal)
	rospy.spin()