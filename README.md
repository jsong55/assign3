# assign3
 assignment 3 for CS 580R

# uploading to git

git add .

git commit -m "commit message"

git push

# pulling from git

git fetch

git pull

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
cd ~/catkin_src
catkin_create_pkg package_name std_msgs rospy actionlib tf geometry_msgs move_base_msgs
catkin_make

roslaunch turtlebot_gazebo turtlebot_world.launch world_file:=.......
roslaunch turtlebot_gazebo amcl_demo.launch map_file:=.......yaml
roslaunch turtlebot_rviz_launchers view_navigation.launch
