from ultralytics import YOLO
import cv2
import os

img_input = "data/sample_frame.jpg"
img_output = "outputs/sample_frame_output.jpg"

def run_detection(image_path, save_path):
    model = YOLO("yolov8n.pt")  
    
    results = model.predict(source=image_path, conf=0.15, imgsz=960, classes=[2], verbose=False)

    result = results[0]
    plotted = result.plot()  
    cv2.imwrite(save_path, plotted)

    names = model.names
    cls_counts = {}
    for c in result.boxes.cls.tolist():
        cls_counts[names[int(c)]] = cls_counts.get(names[int(c)], 0) + 1

    print("Detections:", cls_counts)
    print(f"Saved annotated image to: {save_path}")

if __name__ == "__main__":
    run_detection(img_input, img_output)
   
    