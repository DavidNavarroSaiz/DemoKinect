################################################################################
### Sample program to stream 
### body, body index, color, align color, depth and IR images in 2D using OpenCV
################################################################################
import cv2
import numpy as np
import utils_PyKinectV2 as utils
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectV2
from pykinect2 import PyKinectRuntime

#############################
### Kinect runtime object ###
#############################
kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Body | 
                                         PyKinectV2.FrameSourceTypes_BodyIndex |
                                         PyKinectV2.FrameSourceTypes_Color |
                                         PyKinectV2.FrameSourceTypes_Depth |
                                         PyKinectV2.FrameSourceTypes_Infrared)

depth_width, depth_height = kinect.depth_frame_desc.Width, kinect.depth_frame_desc.Height # Default: 512, 424
color_width, color_height = kinect.color_frame_desc.Width, kinect.color_frame_desc.Height # Default: 1920, 1080
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.avi', -1, 20.0, (424, 512))
i = 1
while True:
    ##############################
    ### Get images from camera ###
    ##############################
    if kinect.has_new_body_frame() and \
       kinect.has_new_body_index_frame() and \
       kinect.has_new_color_frame() :

        body_frame       = kinect.get_last_body_frame()
        body_index_frame = kinect.get_last_body_index_frame()
        color_frame      = kinect.get_last_color_frame()
        
        #########################################
        ### Reshape from 1D frame to 2D image ###
        #########################################
        body_index_img   = body_index_frame.reshape(((depth_height, depth_width))).astype(np.uint8) 
        color_img        = color_frame.reshape(((color_height, color_width, 4))).astype(np.uint8)


        ###############################################
        ### Useful functions in utils_PyKinectV2.py ###
        ###############################################
        align_color_img = utils.get_align_color_image(kinect, color_img)
        resized = cv2.resize(color_img, (424,512), interpolation = cv2.INTER_AREA)
        print("color_img",color_img.shape)
        align_color_img = utils.draw_bodyframe(body_frame, kinect, align_color_img) # Overlay body joints on align_color_img
        print(align_color_img.shape)

        cv2.imshow('align color with body joints', align_color_img) # (424, 512)
        i += 1
        cv2.imwrite('output/depth'+str(i)+'.png',align_color_img)
        # cv2.imwrite('output.png',align_color_img)

        # image = cv2.imread('output.png')
        # out.write(image)

    key = cv2.waitKey(30)
    if key==27: # Press esc to break the loop
        break

# out.release()
kinect.close()
cv2.destroyAllWindows()














