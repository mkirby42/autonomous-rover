from rclpy.node import Node
import rclpy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from ultralytics import YOLO


class YoloNode(Node):
    def __init__(self):
        super().__init__("yolo_node")
        self.bridge = CvBridge()
        self.model = YOLO("/home/matt/ros2_ws/yolov8n.engine", task="detect")
        self.get_logger().info("Loaded TensorRT engine (GPU)")

        self.image_sub = self.create_subscription(
            Image, "/camera/color/image_raw", self.yolo_callback, 10
        )
        self.annotated_pub = self.create_publisher(Image, "/yolo/annotated_image", 10)

    def yolo_callback(self, msg: Image):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
        results = self.model(cv_image, verbose=False)

        for result in results:
            # Log detections
            for box in result.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                label = result.names[cls_id]
                self.get_logger().info(f"{label}: {conf:.2f}")

            # Publish annotated frame for Foxglove
            annotated = result.plot()
            img_msg = self.bridge.cv2_to_imgmsg(annotated, encoding="bgr8")
            img_msg.header = msg.header
            self.annotated_pub.publish(img_msg)


def main(args=None):
    rclpy.init(args=args)
    yolo_node = YoloNode()
    rclpy.spin(yolo_node)
    yolo_node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
