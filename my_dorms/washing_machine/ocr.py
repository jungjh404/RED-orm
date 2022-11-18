import requests
import uuid
import time
import json
import base64
from io import BytesIO
from PIL import Image

api_url = 'https://jt28sdxiqu.apigw.ntruss.com/custom/v1/19256/eb7aa3f426d38372bc4d3e7519e675f3a41f60eaf3ac89d99be08928f491f964/infer'
secret_key = 'eExQVXB4dVl1alVTWEhxYkN3b0lwUWtRT3htUnlUTnU='

def img_ocr(base64_str):
  request_json = {
    'images': [
        {
            'format': 'jpeg',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000)),
    'lang': 'ko'
  }

  payload = {'message': json.dumps(request_json).encode('UTF-8')}
  files = [
    ('file', BytesIO(base64.b64decode(base64_str))),
  ]
  headers = {
    'X-OCR-SECRET': secret_key
  }

  response = requests.request("POST", api_url, headers=headers, data = payload, files = files)
  
  result = None

  result_json = json.loads(response.text)

  if result_json["images"][0]["message"] == "SUCCESS":
    num_ocr = result_json["images"][0]["fields"][0]
    if num_ocr["name"] == "num":
      result = num_ocr["inferText"]
      if result.isdigit():
        return int(result)
  
  return result


if __name__ == "__main__":
  with open('./test.jpeg', 'rb') as img:
    base64_string = base64.b64encode(img.read())
    img_ocr(base64_string)