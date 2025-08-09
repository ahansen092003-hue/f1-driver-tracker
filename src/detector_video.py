from ultralytics import YOLO
import cv2
import time

video_input = "data/sample_videos/hungary2025.mp4"
video_save = "outputs/hungary2025_detected.mp4"

def detect_video(video_path=video_input, save_path=video_save):
    cap = cv2.VideoCapture(video_path)

if __name__ == "__main__":
    detect_video()