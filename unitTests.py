import unittest
import requests

BASE_URL = "https://jmyqdgd43c.execute-api.us-east-1.amazonaws.com/nuevo/billetera"

class TestBilleteraAPI(unittest.TestCase):

    def test_contactos_exito(self):
        payload = {
            "numero_emisor": "99999999",
            "numero_receptor": "888888888",
            "monto": 5,
            "tipo_operacion": "envio"
        }
        response = requests.post(f"{BASE_URL}/contactos", json=payload)
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIn("88888888", body["body"])
        self.assertIn("777777777", body["body"])

    def test_historial_exito(self):
        payload = {
            "numero": "99999999"
        }
        response = requests.post(f"{BASE_URL}/historial", json=payload)
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertEqual(body["nombre"], "Pablito")
        self.assertGreaterEqual(body["saldo"], 0)
        self.assertIsInstance(body["operaciones"], list)

    def test_contactos_error_numero_emisor(self):
        payload = {
            "numero_emisor": "invalid",
            "numero_receptor": "888888888",
            "monto": 5,
            "tipo_operacion": "envio"
        }
        response = requests.post(f"{BASE_URL}/contactos", json=payload)
        # print(response.json())
        response = response.json()
        self.assertNotEqual(response["statusCode"], 200)
        
        self.assertIn("Error", response)

    def test_historial_error_numero(self):
        payload = {
            "numero": "invalid"
        }
        response = requests.post(f"{BASE_URL}/historial", json=payload)
        self.assertNotEqual(response.status_code, 200)
        body = response.json()
        self.assertIn("error", body)

    def test_pagar_error_monto(self):
        payload = {
            "numero_emisor": "99999999",
            "numero_receptor": "888888888",
            "monto": -5,
            "tipo_operacion": "envio"
        }
        response = requests.post(f"{BASE_URL}/pagar", json=payload)
        self.assertNotEqual(response.status_code, 200)
        body = response.json()
        self.assertIn("error", body)

if __name__ == '__main__':
    unittest.main()
