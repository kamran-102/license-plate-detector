from setuptools import setup, find_packages

setup(
    name='license_plate_detection',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow==10.1.0',
        'torch==2.1.2',
        'torchvision==0.16.2',
        'transformers==4.40.0',
        'sentencepiece==0.1.99',
        'ultralytics',
        'numpy',
        'matplotlib',
        'opencv-python',
        'pandas',
        'paddleocr',
        'easyocr',
        'onnx',
        'mysql.connector',
        'mysql-connector-python',
        'paddlepaddle==2.4.2'
    ],
    entry_points={
        'console_scripts': [
            'detect-plates=scripts.detect_plates:main',
            'perform-ocr=scripts.ocr:main',
        ],
    },
)
