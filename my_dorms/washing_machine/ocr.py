import requests
import uuid
import time
import json

api_url = 'https://jt28sdxiqu.apigw.ntruss.com/custom/v1/19256/eb7aa3f426d38372bc4d3e7519e675f3a41f60eaf3ac89d99be08928f491f964/infer'
secret_key = 'eExQVXB4dVl1alVTWEhxYkN3b0lwUWtRT3htUnlUTnU='
image_file = './test.jpeg'

request_json = {
    'images': [
        {
            'format': 'jpeg',
            'name': 'demo'
        }
    ],
    'requestId': str(uuid.uuid4()),
    'version': 'V2',
    'timestamp': int(round(time.time() * 1000))
}

payload = {'message': json.dumps(request_json).encode('UTF-8')}
files = [
  ('file', open(image_file,'rb'))
]
headers = {
  'X-OCR-SECRET': secret_key
}

response = requests.request("POST", api_url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))