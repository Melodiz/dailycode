import unittest

def is_valid_string(s):
    # s = input()
    r_index = s.index('R')
    m_index = s.index('M')
    
    return r_index < m_index
    # return False

class TestTask1(unittest.TestCase):
    def test_valid_strings(self):
        valid_strings = ["RSM", "RMS", "SRM"]
        for s in valid_strings:
            with self.subTest(s=s):
                self.assertTrue(is_valid_string(s), f"'{s}' should be valid")

    def test_invalid_strings(self):
        invalid_strings = ["MSR", "MRS", "SMR"]
        for s in invalid_strings:
            with self.subTest(s=s):
                self.assertFalse(is_valid_string(s), f"'{s}' should be invalid")

    def test_input_length(self):
        with self.assertRaises(ValueError):
            is_valid_string("RSS")
        with self.assertRaises(ValueError):
            is_valid_string("RMS")

    def test_input_characters(self):
        with self.assertRaises(ValueError):
            is_valid_string("ABC")
        with self.assertRaises(ValueError):
            is_valid_string("RSr")

if __name__ == '__main__':
    unittest.main()