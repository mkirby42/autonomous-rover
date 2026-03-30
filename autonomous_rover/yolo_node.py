from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO
import cv2

class YoloNode(Node):
    def __init__(self):
        super().__init__('yolo_node')
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt')
        self.image_sub = self.create_subscription(Image, "/camera/color/image_raw", self.yolo_callback, 10)
        
    def yolo_callback(self, msg: Image):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='passthrough')
        results = self.model(cv_image)
        for result in results:
            boxes = result.boxes  # Boxes object for bounding box outputs
            masks = result.masks  # Masks object for segmentation masks outputs
            keypoints = result.keypoints  # Keypoints object for pose outputs
            probs = result.probs  # Probs object for classification outputs
            obb = result.obb  # Oriented boxes object for OBB outputs
            self.get_logger().info(f'Boxes: {boxes}')
            # self.get_logger().info(f'Masks: {masks}')
            # self.get_logger().info(f'Keypoints: {keypoints}')
            # self.get_logger().info(f'Probs: {probs}')
            # self.get_logger().info(f'OBB: {obb}')


def main(args=None):
    rclpy.init(args=args)

    yolo_node = YoloNode()

    rclpy.spin(yolo_node)

    yolo_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()