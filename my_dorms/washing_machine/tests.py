import base64
from django.test import TestCase
from .ocr import img_ocr


# Create your tests here.
class WashingMachineTest(TestCase):
    def test_ocr(self):
        with open('./washing_machine/test.jpeg', 'rb') as img:
            base64_string = base64.b64encode(img.read())
            self.assertEqual(52, img_ocr(base64_string))
        
        with open('./washing_machine/test.png', 'rb') as img:
            base64_string = base64.b64encode(img.read())
            self.assertEqual(None, img_ocr(base64_string))
            
