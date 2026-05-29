#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

import serial
import math


class JointStateToSerial(Node):

    def __init__(self):

        super().__init__('joint_state_to_serial')

        # SERIAL CONNECTION
        self.serial_port = serial.Serial(
            '/dev/ttyUSB0',
            115200,
            timeout=1
        )

        # LAST RECEIVED POSITIONS
        self.latest_positions = None

        # SUBSCRIBE TO JOINT STATES
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_callback,
            10
        )

        # SEND DATA EVERY 50ms (20Hz)
        self.timer = self.create_timer(
            0.5,
            self.send_serial_data
        )

        self.get_logger().info("Joint Serial Bridge Started")


    def joint_callback(self, msg):

        self.latest_positions = msg.position


    def send_serial_data(self):

        if self.latest_positions is None:
            return

        try:

            servo_angles = []

            for pos in self.latest_positions:

                # radians -> degrees
                deg = math.degrees(pos)

                # map [-90,+90] -> [0,180]
                servo_angle = int(deg + 90)

                # safety clamp
                servo_angle = max(0, min(180, servo_angle))

                servo_angles.append(servo_angle)

            # create serial string
            serial_data = ",".join(map(str, servo_angles)) + "\n"

            # send to arduino
            self.serial_port.write(serial_data.encode())

            self.get_logger().info(f"Sent: {serial_data.strip()}")

        except Exception as e:

            self.get_logger().error(str(e))


def main(args=None):

    rclpy.init(args=args)

    node = JointStateToSerial()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()