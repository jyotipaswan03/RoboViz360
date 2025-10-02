#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class FakeLaser(Node):
    def __init__(self):
        super().__init__('fake_laser')
        self.pub = self.create_publisher(LaserScan, '/scan', 10)
        self.timer = self.create_timer(0.1, self.publish_scan)

    def publish_scan(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'lidar_link'
        msg.angle_min = -math.pi/2
        msg.angle_max = math.pi/2
        msg.angle_increment = math.pi/180
        msg.range_min = 0.1
        msg.range_max = 3.0
        msg.ranges = [3.0]*180
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FakeLaser()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
