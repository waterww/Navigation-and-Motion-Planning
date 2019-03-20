#! /usr/bin/env python

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from distance import get_distance, coor_trans
from numpy import *

class image_converter:
    def __init__(self):
        # self.image_pub = rospy.Publisher("cv_bridge_image", Image, queue_size=1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/depth/image_rect_raw", Image, self.callback)

    def callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data)
            depth_matrix = get_distance(cv_image)
            print depth_matrix.max()
            print coor_trans(depth_matrix)

            
        except CvBridgeError as e:
            print e

        # show the image of opencv
        # cv2.imshow("Image window", cv_image)
        # cv2.waitKey(3)

        # transfer opencv-data-type image into ROS-data-type image
        # try:
            # self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "mono16"))
        # except CvBridgeError as e:
            # print e
if __name__ == '__main__':
    try:
        rospy.init_node("cv_bridge_test")
        rospy.loginfo("Starting cv_bridge_test node")
        image_converter()
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down cv_bridge_test node."
        cv2.destroyAllWindows()
