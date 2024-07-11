import pandas as pd
import cv2
from paddleocr import PaddleOCR
from PIL import Image
import easyocr
# test.py
import torch
from PIL import Image
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')

tokenizer = AutoTokenizer.from_pretrained('openbmb/MiniCPM-Llama3-V-2_5', trust_remote_code=True)
model.eval()


def easy_ocr(image_path):
    img = cv2.imread(f"{image_path}")
    reader = easyocr.Reader(['ar', 'en']) 
    results = reader.readtext(img, detail=0)  # detail=0 returns only the text
    easy_ocr_results = "".join([text for text in results])
    return easy_ocr_results


def paddle_ocr(image_path):
    ocr = PaddleOCR(use_angle_cls=True, lang='ar')
    result = ocr.ocr(image_path, cls=True)
    Paddle_ocr_resutls = [elements[1][0] for elements in result[0]]
    return "".join(Paddle_ocr_resutls)


def MiniCPM_Llama3_ocr(image):
    question = 'please read the text from this image. Please make sure only return 3 English Alphabets and 3 English Numbers. if number of characters is more than 8 than not return garbage data. Please make sure total number of letter never be more than 8.'
    msgs = [{'role': 'user', 'content': question}]

    res = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=tokenizer,
        sampling=True, # if sampling=False, beam_search will be used by default
        temperature=0.7,
        # system_prompt='' # pass system_prompt if needed
    )
    ## if you want to use streaming, please make sure sampling=True and stream=True
    ## the model.chat will return a generator
    res = model.chat(
        image=image,
        msgs=msgs,
        tokenizer=tokenizer,
        sampling=True,
        temperature=0.7,
        stream=True
    )

    generated_text = ""
    for new_text in res:
        generated_text += new_text
    return generated_text

