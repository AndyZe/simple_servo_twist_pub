# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import math
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import TwistStamped


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('simple_servo_twist_pub')
        self.publisher_ = self.create_publisher(TwistStamped, '/servo_node/delta_twist_cmds', 1)
        self.timer_period = 0.05  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.elapsed_time = 0
        self.motion_period = 0.25  # sec

    def timer_callback(self):
        msg = TwistStamped()
        msg.header.stamp = self.get_clock().now().to_msg()
        # Sine wave motion
        self.elapsed_time = self.elapsed_time + self.timer_period
        msg.twist.linear.x = 0.05 * math.sin(2 * math.pi * self.motion_period * self.elapsed_time)
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
