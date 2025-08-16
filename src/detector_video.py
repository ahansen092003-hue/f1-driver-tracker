from ultralytics import YOLO
import cv2
import time

video_input = "data/sample_videos/hungary2025.mp4"
video_save = "outputs/hungary2025_detected.mp4"

def detect_video(video_path, save_path):
    vid_capture = cv2.VideoCapture(video_path)
    if (vid_capture.isOpened() == False):
        print("Error opening the video file")
        return
    
    

if __name__ == "__main__":
    detect_video(video_input, video_save)