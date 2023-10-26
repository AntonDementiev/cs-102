import unittest
from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class VigenereTestCase(unittest.TestCase):

    def test_encrypt_vigenere_upper(self):
        self.assertEqual(encrypt_vigenere(plaintext="PYTHON", keyword="A"), "PYTHON")
    
    def test_decrypt_vigenere_upper(self):
        self.assertEqual(decrypt_vigenere(ciphertext="PYTHON", keyword="A"), "PYTHON")

    def test_encrypt_vigenere_lower(self):
        self.assertEqual(encrypt_vigenere(plaintext="python", keyword="a"), "python")
    
    def test_decrypt_vigenere_lower(self):
        self.assertEqual(decrypt_vigenere(ciphertext="python", keyword="a"), "python")

    def test_encrypt_vigenere_lemon(self):
        self.assertEqual(encrypt_vigenere(plaintext="ATTACKATDAWN", keyword="LEMON"), 'LXFOPVEFRNHR')
    
    def test_decrypt_vigenere_lemon(self):
        self.assertEqual(decrypt_vigenere(ciphertext="LXFOPVEFRNHR", keyword="LEMON"), 'ATTACKATDAWN')
