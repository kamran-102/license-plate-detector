import os
import mysql.connector
from src.utils.dbconnect import db_connect
from scripts.detect_plates import yolo_img_license_plate_detector, yolo_video_license_plate_detector
from config import *
import pandas as pd
import cv2


if process_video == True:
    yolo_video_license_plate_detector(video_path, model_path, tracking_record_csv)
else:
    plate_scanner_df = pd.DataFrame()
    for image_path in os.listdir(f'{img_data_dir}'):
        detection_results = yolo_img_license_plate_detector(f"{img_data_dir}/{image_path}", model_path)    
        #store data to db
        results_df = pd.DataFrame(detection_results)
        # os.remove("test.png")
        if use_data_warehouse == True:
            conn = db_connect(table_is_existed)
            cursor = conn.cursor()
            print(results_df)
            for index,row in results_df.iterrows():
                cursor.execute(f"""
                INSERT INTO plateScanner (
                ImgPath,
                Xmin,
                Ymin,
                Xmax,
                Ymax,
                Confidence,
                PaddleOCR,
                EasyOCR)
                VALUES ('{row.ImgPath}', {int(row.Xmin)}, {int(row.Ymin)}, {int(row.Xmax)}, {int(row.Ymax)}, {row.Confidence}, '{row.PaddleOCR}', '{row.EasyOcr}')""")
            conn.commit()
            conn.close()
            
        else:
            if os.path.exists(f"{annotation_file_path}"):
                plate_scanner_df = pd.read_csv(f"{annotation_file_path}")
                print("yes..............\n.............Yes")
            plate_scanner_df = plate_scanner_df._append(results_df,ignore_index=False)
            plate_scanner_df.to_csv(f"{annotation_file_path}",index=False)



