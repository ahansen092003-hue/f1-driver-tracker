import cv2

vid_capture = cv2.VideoCapture('data/sample_videos/hungary2025.mp4')

if (vid_capture.isOpened() == False):
    print("Error opening the video file")
else:
    fps = int(vid_capture.get(5))
    print("Frame Rate : ",fps,"frames per second") 
    frame_count = vid_capture.get(7)
    print("Frame count : ", frame_count)
    

vid_capture.release()