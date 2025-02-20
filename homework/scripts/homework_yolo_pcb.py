from ultralytics import YOLO
import cv2
import numpy as np
import  os
import torch

model = YOLO("homework/models/best.pt")




def yolo_to_xyxy(label_file, img_width, img_height):
    """
    Converts YOLO format (x_center, y_center, width, height) to (x1, y1, x2, y2)
    """
    with open(label_file, "r") as f:
        lines = f.readlines()

    gt_boxes = []
    for line in lines:
        data = line.strip().split()
        _, x_center, y_center, width, height = map(float, data)

        x1 = (x_center - width / 2) * img_width
        y1 = (y_center - height / 2) * img_height
        x2 = (x_center + width / 2) * img_width
        y2 = (y_center + height / 2) * img_height

        gt_boxes.append([x1, y1, x2, y2])

    return np.array(gt_boxes)


def calculate_iou(box1, box2):
    """
    Compute IoU between two bounding boxes.
    box1, box2: (x1, y1, x2, y2) format
    """
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # Compute intersection area
    intersection = max(0, x2 - x1) * max(0, y2 - y1)

    # Compute union area
    box1_area = (box1[2] - box1[0]) * (box1[3] - box1[1])
    box2_area = (box2[2] - box2[0]) * (box2[3] - box2[1])
    union = box1_area + box2_area - intersection

    return intersection / union if union else 0


def inference_test_set(test_image_paths):
    for img in os.listdir(test_image_paths):
        test_img_path = os.path.join(test_image_paths, img)
        test_label_path = os.path.join(test_image_paths.replace("images", "labels"), os.path.splitext(img)[0] + ".txt")
    
        os.path.basename
        # Run YOLO model
        img = cv2.imread(test_img_path)
        results = model(img)
        gt_boxes = yolo_to_xyxy(test_label_path, 960, 960)

        # Draw Ground Truth
        for (x1, y1, x2, y2) in gt_boxes:
            cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)  

        # Draw Predictions
        for result in results:
            for box in result.boxes.xyxy:
                x1, y1, x2, y2 = map(int, box.tolist())
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)  
        for pred in results[0].boxes.xyxy.tolist():
            for gt in gt_boxes:
                iou = calculate_iou(pred, gt)
                print(f"IoU: {iou:.2f}")

    # Display Image
        cv2.imshow("Comparison", img)
        cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    test_images = "homework/dataset/pcb_defects.v4i.yolov11/test/images"
    inference_test_set(test_image_paths=test_images)