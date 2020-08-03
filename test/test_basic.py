from unittest import TestCase
import Hencoder


class TestHencoder(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Calling Testcase constructor
        self.encoded = "00101101000101110011010110101101010000011011000010000100000000011000110101110100"
        self.string = "Akash"

    def test_encode(self):
        output = Hencoder.encode(self.string)
        self.assertEqual(
            self.encoded, output, "Encode function not working as desired."
        )

    def test_decode(self):
        output = Hencoder.decode(self.encoded)
        self.assertEqual(self.string, output, "Decode function not working as desired.")
