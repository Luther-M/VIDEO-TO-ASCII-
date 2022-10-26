import cv2 
from cv2 import cvtColor,resize
import numpy as np

ascii_characters_by_surface = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def convert_ascii_index(value):
    brightness_weight= len(ascii_characters_by_surface)/256
    index = int(float(value)*brightness_weight)
    return index

def show_ascii(value):
    print(ascii_characters_by_surface[value],end="")


def main():
    cap = cv2.VideoCapture("lagtrain.mp4")               # Change lagtrain.mp4 to another video with .mp4 at end

    if(cap.isOpened() ==False):
        print("Error opening video stream or file")

    while(cap.isOpened()):
        ret,frame =cap.read()
        if ret ==True:
            gray = cvtColor(frame, cv2.COLOR_BGR2GRAY)
            img = resize(gray,(180,60))

            for i, x in enumerate(img):
                for j, a in enumerate(x):
                    img[i][j]=convert_ascii_index(a)
                    
            for i, x in enumerate(img):
                for j, a in enumerate(x):
                    show_ascii(a)
                print()
            
            if cv2.waitKey(30) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
