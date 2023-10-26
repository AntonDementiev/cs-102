import unittest
from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class CaesarTestCase(unittest.TestCase):

    def test_encrypt_caesar_lower(self):
        self.assertEqual(encrypt_caesar(plaintext='python', shift=3), 'sbwkrq')
    
    def test_decrypt_caesar_lower(self):
        self.assertEqual(decrypt_caesar(ciphertext='sbwkrq', shift=3), 'python')
    
    def test_encrypt_caesar_upper(self):
        self.assertEqual(encrypt_caesar(plaintext="PYTHON", shift=3), 'SBWKRQ')
    
    def test_decrypt_caesar_upper(self):
        self.assertEqual(decrypt_caesar(ciphertext="SBWKRQ", shift=3), 'PYTHON')

    def test_encrypt_caesar_numbers(self):
        self.assertEqual(encrypt_caesar(plaintext="Python3.6", shift=3), 'Sbwkrq3.6')
    
    def test_decrypt_caesar_numbers(self):
        self.assertEqual(decrypt_caesar(ciphertext="Sbwkrq3.6", shift=3), 'Python3.6')
    
    def test_encrypt_caesar_empty(self):
        self.assertEqual(encrypt_caesar(plaintext="", shift=3), '')
    
    def test_decrypt_caesar_empty(self):
        self.assertEqual(decrypt_caesar(ciphertext="", shift=3), '')