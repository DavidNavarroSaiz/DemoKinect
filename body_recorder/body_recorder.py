from pykinect_body_detector import BodyDetector
from video_recorder import VideoRecorder
import cv2
Is_done = False
body_image = BodyDetector()
id_video = '0001' # en la base de datos esta relacionado con el nombre del paciente, terapia, etc..

recorder = VideoRecorder(id_video)
while not Is_done:
    image = body_image.run()
    recorder.append_frame(image)
    cv2.imshow('color', image)
    key = cv2.waitKey(10)
    if key==27: # Press esc to break the loop
        recorder.finish_record()
        body_image.finish_detection()
        Is_done = True
