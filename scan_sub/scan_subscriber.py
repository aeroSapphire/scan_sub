#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class ScanSubscriber(Node):
    
    def __init__(self):
        super().__init__("scan_subscriber")
        self.scan_subscriber = self.create_subscription(LaserScan, "/scan", self.scan_callback, 10)

    def scan_callback(self, msg: LaserScan):
        self.get_logger().info(str(msg))


def main(args=None):
    rclpy.init(args=args)
    node = ScanSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
