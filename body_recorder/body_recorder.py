from pykinect_body_detector import BodyDetector
from video_recorder import VideoRecorder
import cv2
Is_done = False
id_video = '0003' # en la base de datos esta relacionado con el nombre del paciente, terapia, etc..
body_image = BodyDetector()
recorder = VideoRecorder(id_video)
while not Is_done:
    image = body_image.run()
    recorder.append_frame(image)
    cv2.imshow('color', image)
    key = cv2.waitKey(10)
    if key==27 or key == 25: # Press esc or Q to break the loop
        recorder.finish_record()
        body_image.finish_detection()
        Is_done = True
