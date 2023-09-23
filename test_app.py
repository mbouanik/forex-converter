from unittest import TestCase
from app import app


class TestApp(TestCase):
    def test_home(self):
        with app.test_client() as client:
            res = client.get("/")
            data = res.get_data(as_text=True)
            self.assertEqual(200, res.status_code)
            self.assertIn("Forex", data)

    def test_converter(self):
        with app.test_client() as client:
            res = client.post(
                "/converter", data={"currency_one": "USD", "currency_two": "USD" "amount":100}
            )
            self.assertEqual(res.status_code, 200)
            self.assertIn("$100", res.get_data(as_text=True))
