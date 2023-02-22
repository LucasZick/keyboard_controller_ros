# Keyboard Controller ROS
keyboard_controller_ros is a ROS package designed to allow controlling robots using a keyboard. It includes a simple Python script that reads key presses and publishes them as ROS messages. These messages can then be received by a robot controller node, allowing the robot to be controlled in real-time.

## Installation
To use keyboard_controller_ros, first clone the repository to your ROS workspace:

```
cd ~/catkin_ws/src
git clone https://github.com/your_username/keyboard_controller_ros.git
```
Then, build the package using catkin_make:

```
cd ~/catkin_ws
catkin_make
```

## Usage
To use keyboard_controller_ros, run the keyboard_controller.py script:

```
rosrun keyboard_controller_ros keyboard_controller.py
```

This will start the keyboard controller node, which will read key presses and publish them as ROS messages.

To receive these messages and control your robot, you will need to implement a ROS node that subscribes to the keyboard topic and responds to the key presses appropriately.


## Contributing

Contributions to keyboard_controller_ros are welcome! If you find a bug or have an idea for a new feature, please submit an issue or pull request on GitHub.

## License

keyboard_controller_ros is released under the MIT license. See the LICENSE file for more information.
