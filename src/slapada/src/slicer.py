import cv2

class Slicer():


    @staticmethod
    def slice(filename: std, path: str):
        
        vidcap = cv2.VideoCapture(path)
        success,image = vidcap.read()
        count = 0
        while success:
            cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
            success,image = vidcap.read()
            print('Read a new frame: ', success)
            count += 1
