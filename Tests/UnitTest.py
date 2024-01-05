"""
Author : Sudharsan Vishvanath
Contact : L00179143@atu.ie
Purpose : Tutorials and demonstration for Lists in python programming
Pre-requisites : Python3 installation.
"""

import unittest
import formatter

class TestFormatter(unittest.TestCase):
    def test_lower(self):
        test_text = "Sudharsan Vishvanath"
        result = formatter.convert_lower(test_text)
        self.assertEqual(result, "sudharsan vishvanath")

    def test_upper(self):
        test_text = "Sudharsan Vishvanath"
        result = formatter.convert_upper(test_text)
        self.assertEqual(result, "SUDHARSAN VISHVANATH")

if __name__ =="__main__":
    unittest.main()