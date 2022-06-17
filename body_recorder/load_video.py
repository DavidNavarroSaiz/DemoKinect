import cv2
class LoadVideo():
    def __init__(self,patient_id): 
        self.fps = 60
        self.video_path = patient_id + '.avi'
        self.video_scr = cv2.VideoCapture(self.video_path)
        self.run()
    def run(self):
        while(True):
            ret, frame = self.video_scr.read()
            if ret == True:
                cv2.imshow('Frame',frame)
                cv2.waitKey(10)
            else:
                print("Video failed")
                break
                
        self.video_scr.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    video = LoadVideo('0003')


       
