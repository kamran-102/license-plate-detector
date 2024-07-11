import os
import random
import numpy as np
from ultralytics import YOLO
import matplotlib.pyplot as plt
import hashlib
from scripts.preprocess import image_pre_processing
import csv
from scripts.postprocess import english_to_arabic_mapping
from scripts.ocr import *
from PIL import Image
import datetime
import cv2

def yolo_img_license_plate_detector(image_path, model_path):
    model = YOLO(f'{model_path}')
    results = model(f'{image_path}', save=False, show_labels=True)
    nb_plates_data = []
    print(results[0])
    print(nb_plate.orig_img)
    for nb_plate in results[0]:
        image = nb_plate.orig_img
        x1, y1, x2, y2 = np.array(nb_plate.boxes.xyxy.cpu().squeeze())
        print(x1, y1, x2, y2)
        # Crop the image using array slicing
        cropped_image = image[int(y1):int(y2), int(x1):int(x2)]
        img = Image.fromarray(cropped_image, 'RGB')
        image_hash_name = hashlib.md5(str(datetime.datetime.now()).encode()).hexdigest()
        detected_image_path = f'test.png'
        img.save(f'{detected_image_path}')
        #image preprocessing
        # image_pre_processing(f'{detected_image_path}')
        #ocr image
        try:
            easy_ocr_results = easy_ocr(f'{detected_image_path}')
        except:
            easy_ocr_results = ""
        try:
            paddle_ocr_results = paddle_ocr(f'{detected_image_path}')
        except:
          paddle_ocr_results = ""
        try:
            MiniCPM_Llama3_ocr_results = MiniCPM_Llama3_ocr(img)
            arabic_ocr = english_to_arabic_mapping(MiniCPM_Llama3_ocr_results)
        except:
            MiniCPM_Llama3_ocr_results = ""
            arabic_ocr = ""
        confidence = nb_plate.boxes.conf.item()
        # if float(confidence) > 0.2:
        nb_plates_data.append({"ImgPath": f"{image_path}", "Xmin":int(x1), "Ymin": int(y1), "Xmax":int(x2), "Ymax":int(y2), "Confidence": confidence, "EasyOCR": easy_ocr_results, "PaddleOCR": paddle_ocr_results, "MiniCPM_Llama3_OCR":MiniCPM_Llama3_ocr_results, "Arabic-OCR":arabic_ocr})
        # else:
        #     return []
    return nb_plates_data


def yolo_video_license_plate_detector(video_path, model_path, tracking_record_csv):
    model = YOLO(f'{model_path}')
    cap = cv2.VideoCapture(f'{video_path}')  

    # Open a CSV file to write tracking records
    with open(f'{tracking_record_csv}', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['Frame', 'Class', 'Confidence', 'X1', 'Y1', 'X2', 'Y2', 'OCR', 'Arabic-OCR'])

        frame_number = 0

        while True:
            # Read a new frame
            ret, frame = cap.read()
            if not ret:
                break

            # Use YOLOv8 model to make predictions
            results = model(frame)

            # Iterate through the detected objects
            for result in results:
                boxes = result.boxes.xyxy.cpu().numpy()  # Bounding box coordinates
                confidences = result.boxes.conf.cpu().numpy()  # Confidence scores
                classes = result.boxes.cls.cpu().numpy()  # Class labels

                for i in range(len(boxes)):
                    x1, y1, x2, y2 = boxes[i]
                    cropped_image = frame[int(y1):int(y2), int(x1):int(x2)]
                    img = Image.fromarray(cropped_image, 'RGB')
                    try:
                        MiniCPM_Llama3_ocr_results = MiniCPM_Llama3_ocr(img)
                        arabic_ocr = english_to_arabic_mapping(MiniCPM_Llama3_ocr_results)
                    except:
                        MiniCPM_Llama3_ocr_results = ""
                        arabic_ocr = ""

                    confidence = confidences[i]
                    class_id = int(classes[i])
                    # Write the tracking record to the CSV file
                    writer.writerow([frame_number, class_id, confidence, x1, y1, x2, y2, MiniCPM_Llama3_ocr_results, arabic_ocr])

                    # # Draw bounding box on the frame
                    # cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
                    # cv2.putText(frame, f'{class_id} {confidence:.2f}', (int(x1), int(y1) - 10),
                    #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Increment frame number
            frame_number += 1

            # # Display the frame
            # cv2.imshow('Tracking', frame)

            # Exit if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the video capture object
    # cap.release()
    # cv2.destroyAllWindows()

