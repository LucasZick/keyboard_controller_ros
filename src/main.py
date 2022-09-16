#PRA RODAR, SETAR DOIS TERMINAIS,
#   UM COM O CODIGO: roscore
#   OUTRO COM O CODIGO: rosrun turtlesim turtlesim_node 

import asyncio
import os
import sys
import time
import rospy
from geometry_msgs.msg import Twist

from src.job import job

class run():
    def __init__(self):
        self.vel_linear = 1
        self.vel_angular = 1

    def load_app(self):
        os.system('rosservice call /reset')
        os.system("clear")
        print('Setting up the application...')
        time.sleep(2)
        os.system("clear")
    
    def close_app(self):
        os.system("clear")
        print("Closing application...")
        time.sleep(2)
        os.system("clear")
        sys.exit(0)

    vel_linear = 1
    vel_angular = 1

    def set_vel_linear(self, foo):
        self.vel_linear = foo

    def set_vel_angular(self, foo):
        self.vel_angular = foo

    def get_vel_linear(self):
        return self.vel_linear

    def get_vel_angular(self):
        return self.vel_angular

    def main(self):
        try:
            rospy.init_node('turtle_controller', anonymous=True)
            pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=50)
            while not rospy.is_shutdown():
                asyncio.run(job(pub, self))
        except Exception as err:
            print(f"Error: Unreadable entry {err}")
            self.main()


if __name__ == "src.main":
    app = run()
    app.load_app()
    app.main()
