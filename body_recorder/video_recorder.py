
import cv2
class VideoRecorder():
    def __init__(self,name):
        self.name = name
        self.fps = 60
        self.width,self.height = 768, 432
        self.color_frames = []
        self.color_out = cv2.VideoWriter(
                name + '.avi',
                cv2.VideoWriter_fourcc(*'DIVX'),
                self.fps,
                (self.width, self.height)
              )
        
    def append_frame(self,image):
        self.color_frames.append(image)

    def finish_record(self):
        for frame in self.color_frames:
            self.color_out.write(frame)
        print(f"Record{self.name} Saved")
        self.color_out.release()

    