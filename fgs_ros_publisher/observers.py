# -*- coding: utf-8 -*-
import numpy as np
import cv_bridge
import rclpy
from rclpy.node import Node
from rclpy.time import Time
from sensor_msgs.msg import Image


class ObservationChain(object):
    def __init__(self):
        self._observes = list()

    def add_observer(self, observe):
        self._observes.append(observe)

    def event(self, subject):
        neo_subject = subject
        for observe in self._observes:
            neo_subject = observe(neo_subject)
            if neo_subject is None:
                return


class CVBridgeObserver(object):
    def __init__(self, frame_id):
        self._frame_id = frame_id
        self._bridge = cv_bridge.CvBridge()

    def event(self, subject):
        if type(subject) is not np.ndarray:
            return None

        cv_msg = self._bridge.cv2_to_imgmsg(subject, 'bgr8')
        cv_msg.header.frame_id = self._frame_id
        # cv_msg.header.stamp = Time.now()

        return cv_msg



class ImagePublisher(Node):
    def __init__(self):
        super().__init__('img_pub')
        self._pub = self.create_publisher(Image, 'image', 1)

    def event(self, subject):
        self._pub.publish(subject)
