
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, ReliabilityPolicy, HistoryPolicy, DurabilityPolicy





class scanfilter(Node):

    def __init__(self):
        super().__init__('laser_filter')

        qos_profile = QoSProfile(
            reliability=ReliabilityPolicy.BEST_EFFORT,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            history=HistoryPolicy.KEEP_LAST,
            depth=1
        )

        self.scan_sub= self.create_subscription(
            LaserScan,
            '/upper_camera/image_raw',
            self.process_data,qos_profile)
        


        self.scan_pub=self.create_publisher(LaserScan,"/filtered_scan",qos_profile)
        self.laser_data=LaserScan()

        

        self.timer=self.create_timer(0.1,self.timer_callback)

    def process_data(self, data):
        self.laser_data=data
        self.laser_data.range_min=0
        self.laser_data.range_max=120


    def timer_callback(self):

        self.scan_pub.publish(self.laser_data)
        
            
        


def main(args=None):
    rclpy.init(args=args)

    scan_filter = scan_filter()

    rclpy.spin(scan_filter)

    rclpy.shutdown()


if __name__ == '__main__':
    main()