import cv2
import numpy as np
import os

# --- Simplified SORT tracker class ---
class SimpleSortTracker:
    def __init__(self):
        self.trackers = {}
        self.next_id = 0

    def update(self, detections):
        newtrackers = {}
        for det in detections:
            newtrackers[self.next_id] = det[:4]  # store bbox only
            self.next_id += 1
        self.trackers = newtrackers
        return list(self.trackers.items())

# --- Load YOLOv3 (check for files) ---
use_yolo = all(os.path.exists(f) for f in ["yolov3.weights", "yolov3.cfg", "coco.names"])
if use_yolo:
    print("✅ YOLOv3 model found. Loading...")
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]
else:
    print("⚠️ YOLO files not found. Using mock detections for demo.")
    net, classes, output_layers = None, ["person", "car", "dog"], []

# --- Camera setup ---
video_path = 0  # 0 for webcam, or replace with filename
cap = cv2.VideoCapture(video_path)
tracker = SimpleSortTracker()

if not cap.isOpened():
    print("❌ Cannot open video source.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]
    detections = []

    if use_yolo:
        # --- Object detection (YOLO) ---
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        outs = net.forward(output_layers)

        boxes, confidences, class_ids = [], [], []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        if len(indexes) > 0:
            for i in indexes.flatten():
                x, y, w, h = boxes[i]
                detections.append([x, y, x + w, y + h, confidences[i], class_ids[i]])
    else:
        # --- Mock detections (for demo without YOLO files) ---
        detections = [[100, 100, 200, 200, 0.9, 0], [300, 150, 400, 300, 0.8, 1]]

    # --- Tracking ---
    tracked = tracker.update(detections)

    # --- Draw results ---
    for track_id, bbox in tracked:
        x1, y1, x2, y2 = map(int, bbox)
        label = "object"
        conf = 0
        if detections and track_id < len(detections):
            class_id = int(detections[track_id][5])
            label = classes[class_id] if class_id < len(classes) else "obj"
            conf = detections[track_id][4]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} ID:{track_id}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Object Detection & Tracking", frame)
    print(f"Frame processed. Detections: {[classes[int(d[5])] for d in detections]} IDs: {[tid for tid, _ in tracked]}")

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
print("\n--- Real-time object detection and tracking completed. ---")
