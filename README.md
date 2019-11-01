# Assignment 3 CS 580R

By Nicholas Abate and Jiaxu Song

## Launch files included

assign3_bringup.launch - Launching this file will bringup the turtlebot and get it ready to take an rviz pose.

assign3_navigation.launch - Launching this file will begin autonomous navigation.

assign3_voice.launch - Launching this file will bring up the voice command controller.

## Included packages

There are two packages included in this submission.

### assign3

Assign3 contains code for SLAM, Rviz integration, and autonomous navigation. It also contains the launch files described above.

### pocketsphinx

The pocketsphinx package is a slight modification from the open-source ROS kinetic pocketsphinx package. This package allows for voice recognition and commands. When using this code, make sure to follow the README.md in this package to ensure all dependencies are installed.
