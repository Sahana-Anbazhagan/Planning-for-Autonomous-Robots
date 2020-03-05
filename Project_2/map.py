"""Obstacle map
"""
import cv2
import numpy as np

# placeholder
class Map:
    def __init__(self, xbounds=[0, 300], ybounds=[0, 200]):
        self.xbounds = xbounds
        self.ybounds = ybounds

    def isvalid(self, vertex):
        # return true if the given vertex is not an obstacle and is
        #  within the workspace bounds
        return ((self.xbounds[0] < vertex[0] < self.xbounds[1]) and (self.ybounds[0] < vertex[1] < self.ybounds[1]))

    # cv2.imshow("Final Map", blank_image)
    blank_image = 255 * np.ones(shape=[200, 300, 3], dtype=np.uint8)
    # Window name in which image is displayed
    map = 'Map with obstacles'

    # Drawing the obstacles
    # Circular Obstacle
    cir_center = (225, 50) # Center coordinates of the circular obstacle
    r = 25 # Radius of circular obstacle
    outline_color = (0, 0, 0) # black color for the obstacle outline
    # Draw a circular obstacle on the map
    circle = cv2.circle(blank_image, cir_center, r, outline_color, 1)

    # Elliptical Obstacle
    el_center = (150, 100) # Center coordinates of the ellipse shaped obstacle
    el_major = 40 # Major axis length of the ellipse
    el_minor = 20 # Minor axis length of the ellipse
    # Draw an ellipse shaped obstacle on the map
    ellipse = cv2.ellipse(blank_image, el_center, (el_major, el_minor), 0, 0, 360, 0, 1)

    # Polygon Obstacle
    poly = np.array([[20, 80], [25, 15], [75, 15], [100, 50], [75,80], [50,50]], np.int32) # Vertices of the polygon
    # Draw the polygon, True indicates it is a closed line polygon
    polygon = cv2.polylines(blank_image, [poly], True, outline_color)

    # Diamond shaped obstacle
    vertices = np.array([[225,190], [250,175], [225,160], [200,175]], np.int32) # Vertices of the diamond
    #Draw the diamond shaped obstacle
    diamond = cv2.polylines(blank_image,[vertices], True, outline_color)

    # Displaying the final map with obstacles
    cv2.imshow(map, diamond)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''    # The rectangular obstacle (Working on it)
    rot_rect = ([[95, 170], [10, 75]], 30)
    rectangle = cv2.polylines(blank_image,rot_rect,True, outline_color)
'''
