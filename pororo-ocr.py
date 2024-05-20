import warnings
from pororo import Pororo
from google.cloud import translate_v2 as translate
import os

warnings.filterwarnings("ignore", message="Default grid_sample and affine_grid behavior has changed")

key_path = r"C:\Users\gk12f\OneDrive\바탕 화면\test\ictgcp001-7d5b3d756d02.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# Pororo OCR
ocr = Pororo(task="ocr", lang="ko")

image_path = "test.jpeg"
extracted_text = ocr(image_path)

print("추출한 텍스트:", extracted_text)


if isinstance(extracted_text, list):
    extracted_text = " ".join(extracted_text)


translate_client = translate.Client()

# 한국어 -> 영어
result = translate_client.translate(extracted_text, source_language='ko', target_language='en')

# 번역된 텍스트 출력
print("번역된 텍스트:", result['translatedText'])
