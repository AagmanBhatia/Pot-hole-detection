from ultralytics import YOLO
import cv2
import numpy as np

# Load a model
model = YOLO("best.pt")
class_names = model.names

# Open the video file
cap = cv2.VideoCapture('test_road2.mp4')

while True:
    # Read a frame from the video
    ret, img = cap.read()
    
    # Break the loop if the frame was not read correctly
    if not ret:
        break
    
    # Resize the image
    img = cv2.resize(img, (1020, 500))
    h, w, _ = img.shape
    
    # Predict using the YOLO model
    results = model.predict(img)
    
    for r in results:
        boxes = r.boxes  # Boxes object for bbox outputs
        masks = r.masks  # Masks object for segment masks outputs
        
    if masks is not None:
        masks = masks.data.cpu()
        for seg, box in zip(masks.data.cpu().numpy(), boxes):
            seg = cv2.resize(seg, (w, h))
            contours, _ = cv2.findContours((seg).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in contours:
                d = int(box.cls)
                c = class_names[d]
                x, y, x1, y1 = cv2.boundingRect(contour)
                cv2.polylines(img, [contour], True, color=(0, 0, 255), thickness=2)
                cv2.putText(img, c, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                 
    cv2.imshow('img', img)
    
    # Break the loop on pressing 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video file and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
