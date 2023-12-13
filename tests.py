from app import app
from unittest import TestCase

class ConverterTestCase(TestCase):
    def test_converter(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)
    
    def test_form(self):
        with app.test_client() as client:
            res = client.post('/', data={"from": app.starting})
            html = res.get_data(as_text=True)

            res = client.post('/', data={"to": app.ending})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200) 
            self.assertIn("f'<h1>Converted Amount: {ending_symbol}{rounded_conversion}'", html)