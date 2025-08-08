import cv2

vid_capture = cv2.VideoCapture('data/sample_videos/hungary2025.mp4')

if (vid_capture.isOpened() == False):
    print("Error opening the video file")
else:
    fps = int(vid_capture.get(cv2.CAP_PROP_FPS))
    total_frames = int(vid_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"✅ Opened video. FPS: {fps}, Total Frames: {total_frames}")

    # Grab the 100th frame
    vid_capture.set(cv2.CAP_PROP_POS_FRAMES, 1000)
    ret, frame = vid_capture.read()

    if ret:
        print("✅ Successfully read one frame.")
        cv2.imwrite("data/sample_frame.jpg", frame)
    else:
        print("❌ Failed to read frame.")

    vid_capture.release()