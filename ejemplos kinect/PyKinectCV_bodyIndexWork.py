from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2, sys

if sys.hexversion >= 0x03000000:
    import _thread as thread
else:
    import thread

class BodyGameRuntime(object):
    def __init__(self):
        #create a black image # back buffer surface for drawing skeletons
        self._frame_surface = np.zeros((1080,1920,3), np.uint8)  #960      540

        # Loop until the user clicks the close button.
        self._done = False

        # Kinect runtime object, we want only color and body frames 
        self._kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color |  PyKinectV2.FrameSourceTypes_BodyIndex)
        
        # here we will store skeleton data 
        self._bodies = None   
    
    def run(self):
        # -------- Main Program Loop -----------
        while not self._done:
            # --- Getting frames and drawing  
            # --- Woohoo! We've got a color frame! Let's fill out back buffer surface with frame's data 
            if self._kinect.has_new_body_index_frame():
                frame = self._kinect.get_last_color_frame()
                bi_frame = self._kinect.get_last_body_index_frame()
                body_index_img   = bi_frame.reshape(((424, 512))).astype(np.uint8)
                cv2.imshow('BI img', body_index_img)
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self._done = True

        # Close our Kinect sensor, close the window and quit.
        self._kinect.close()
        cv2.destroyAllWindows()

__main__ = "Kinect v2 Body Game"
game = BodyGameRuntime();
game.run();
