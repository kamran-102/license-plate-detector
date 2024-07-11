#Process Video True if you want to work on Video Else False
process_video = False

#DataWareHose
use_data_warehouse = False

#annoation csv file path if you are not using data warehouse
annotation_file_path = 'data/annotations/plateScanner.csv'

#Images Directory Path
img_data_dir = "/content/pics/"
#video path
video_path = 'data/raw_data/1.mp4'
# Video tracking record CSV path
tracking_record_csv = 'data/tracking_records.csv'
# Model Path
model_path = "src/models/license_plate_detector.pt"

# --------------------------------------------------------------------------
# if table name plateScanner is existed in database and contains features , 
# ImgPath,  Xmin, Ymin, Xmax, Ymax, Confidence, Country, PaddleOCR,  EasyOCR
# --------------------------------------------------------------------------
table_is_existed = True
#host
host = 'localhost'
#database Name
database = 'PlateScanDB'
#User Name
username = 'root'
#password
password = 'password'
#tableName
table_name = 'plateScanner'
